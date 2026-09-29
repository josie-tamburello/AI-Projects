import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

def clean_country(country):
    """Standardize country names and filter for U.S. respondents."""
    if pd.isna(country) or str(country).strip() == '':
        return "Not Specified"
    country = str(country).strip().lower()
    if country in ["united states of america", "united states", "usa", "us", "u.s.", "u.s.a."]:
        return "United States"
    return "Other"

def clean_gender(gender):
    """Consolidate gender responses into standardized categories."""
    if pd.isna(gender) or str(gender).strip() == '':
        return "Not Specified"
    gender = str(gender).lower().strip()
    if "female" in gender:
        return "Female"
    elif "male" in gender:
        return "Male"
    return "Other"

def clean_employment(employment):
    """Standardize employment status responses."""
    if pd.isna(employment) or str(employment).strip() == '':
        return "Not Specified"
    employment = str(employment).strip()
    if employment == "0":
        return "Employee"
    elif employment == "1":
        return "Self-Employed"
    return "Other"

def clean_age(age):
    """Filter respondents between 18-65 years old and return whole numbers."""
    try:
        age = int(float(age))  
        if 18 <= age <= 65:
            return str(age)  
        else:
            return None  
    except:
        return None

def clean_tech_company(value):
    """Keep only '1' values and remove '0' and None."""
    try:
        value = str(int(float(value))).strip()  
        return "Tech Company" if value == "1" else None  
    except:
        return None

def clean_and_filter_data(df):
    df = df.copy()
    df.columns = df.columns.str.lower()
    
    df['country'] = df['country'].apply(clean_country)
    df['gender'] = df['gender'].apply(clean_gender)
    df['employment'] = df['employment'].apply(clean_employment)
    df['age'] = df['age'].apply(clean_age)
    df['tech_company'] = df['tech_company'].apply(clean_tech_company)
    
  
    df = df.dropna(subset=['tech_company'])
    
    df_filtered = df[
        (df['age'].notna()) &  
        (df['country'] == "United States") &  
        (df['employment'] == "Employee") & 
        (df['tech_company'].notna())  
    ].reset_index(drop=True)
    
    return df_filtered

def plot_demographic_summary(df_filtered):  
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Sociodemographic Distribution of employees in US Tech Industry', 
                fontsize=14, y=1.02)

    axes = axes.flatten()


    age_groups = pd.cut(pd.to_numeric(df_filtered['age']), 
                       bins=[18, 24, 34, 44, 54, 65],
                       labels=['18-24', '25-34', '35-44', '45-54', '55-65'])
    age_dist = age_groups.value_counts().sort_index()
    sns.barplot(x=age_dist.index, y=age_dist.values, ax=axes[0], palette='Set2')
    axes[0].set_title('Age Distribution', fontsize=10)
    axes[0].tick_params(axis='x', rotation=45)

    gender_dist = df_filtered['gender'].value_counts()
    sns.barplot(x=gender_dist.index, y=gender_dist.values, ax=axes[1], palette='Set2')
    axes[1].set_title('Gender Distribution', fontsize=10)

    state_dist = df_filtered['us_state'].value_counts().head(10)
    sns.barplot(x=state_dist.index, y=state_dist.values, ax=axes[2], palette='Set2')
    axes[2].set_title('Top 10 States', fontsize=10)
    axes[2].tick_params(axis='x', rotation=45)


    year_dist = df_filtered['surveyid'].value_counts().sort_index()
    sns.barplot(x=year_dist.index, y=year_dist.values, ax=axes[3], palette='Set2')
    axes[3].set_title('Survey Year Distribution', fontsize=10)
    axes[3].tick_params(axis='x', rotation=45)

    for ax in axes:
        for p in ax.patches:
            ax.annotate(f'{int(p.get_height())}', 
                       (p.get_x() + p.get_width()/2., p.get_height()),
                       ha='center', va='bottom', fontsize=8)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.set_xlabel('')
        ax.set_ylabel('Count', fontsize=8)
        ax.tick_params(axis='both', which='major', labelsize=8)


    plt.tight_layout()
    plt.show()

    age_stats = pd.to_numeric(df_filtered['age']).describe()
    summary_df = pd.DataFrame({
        'Age': [
            f"{age_stats['min']:.0f}",
            f"{age_stats['25%']:.0f}",
            f"{age_stats['50%']:.0f}",
            f"{age_stats['mean']:.0f}",
            f"{age_stats['75%']:.0f}",
            f"{age_stats['max']:.0f}",
            f"{age_stats['count']:.0f}",
            f"{age_stats['std']:.0f}"
        ]
    }, index=['Min', '1st Quartile', 'Median', 'Mean', '3rd Quartile', 'Max', 'n', 'SD'])
    
    return summary_df