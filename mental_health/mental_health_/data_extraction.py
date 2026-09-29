import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore', category=UserWarning)

def get_db_connection(db_path='/Users/josietamburello/Desktop/NumPy/mental_health/mental_health.sqlite'):
    return sqlite3.connect(db_path)

def get_table_names(conn):
    query = "SELECT name FROM sqlite_master WHERE type='table';"
    return pd.read_sql(query, conn)

def get_table_schema(conn):
    df_tables = get_table_names(conn)
    table_names = df_tables["name"].tolist()
    
    for table in table_names:
        query = f"PRAGMA table_info({table});"
        df_columns = pd.read_sql(query, conn)
        column_names = df_columns["name"].tolist()
        print(f"Columns in {table}:", column_names)
        
def get_total_respondents(conn):
    query = """
    SELECT COUNT(DISTINCT UserID) AS Respondents
    FROM Answer;
    """
    return pd.read_sql(query, conn)

def get_respondents_per_year(conn):
    query = """
    SELECT 
        s.SurveyID AS Year, 
        COUNT(DISTINCT a.UserID) AS Respondents
    FROM Answer a
    JOIN Survey s ON a.SurveyID = s.SurveyID
    GROUP BY s.SurveyID
    ORDER BY s.SurveyID;
    """
    return pd.read_sql(query, conn)

def analyse_question_availability(conn):
    query = """
    SELECT DISTINCT
        q.questionid AS QuestionID,
        q.QuestionText AS Questions, 
        s.SurveyID AS Year
    FROM Answer a
    JOIN Question q ON a.QuestionID = q.QuestionID
    JOIN Survey s ON a.SurveyID = s.SurveyID
    GROUP BY q.QuestionID, q.QuestionText, s.SurveyID
    ORDER BY q.QuestionID, s.SurveyID;
    """
    
    df_questions = pd.read_sql(query, conn)
    df_questions["Year"] = df_questions["Year"].astype(str)
    
    total_years = df_questions["Year"].nunique()
    
    question_counts = (df_questions
                      .groupby(["QuestionID", "Questions"])
                      .agg(Year_Count=("Year", "nunique"))
                      .reset_index())
    
    df_full_questions = question_counts[question_counts["Year_Count"] == total_years]
    df_partial_questions = question_counts[question_counts["Year_Count"] < total_years]
    
    df_full_questions = df_full_questions.sort_values("QuestionID")
    
    return df_full_questions, df_partial_questions, total_years


def get_age_distribution(conn):
    query = """
    SELECT 
        s.SurveyID AS Year, 
        a.AnswerText AS AgeResponse, 
        COUNT(*) AS ResponseCount
    FROM Answer a
    JOIN Question q ON a.QuestionID = q.QuestionID
    JOIN Survey s ON a.SurveyID = s.SurveyID
    WHERE q.QuestionText = 'What is your age?'
    GROUP BY s.SurveyID, a.AnswerText
    ORDER BY s.SurveyID, ResponseCount DESC;
    """
    
    df_age = pd.read_sql(query, conn)
    
    def group_age(age):
        try:
            age = int(age)  
            if age < 18:
                return "Under 18"
            elif 18 <= age <= 24:
                return "18-24"
            elif 25 <= age <= 34:
                return "25-34"
            elif 35 <= age <= 44:
                return "35-44"
            elif 45 <= age <= 54:
                return "45-54"
            elif 55 <= age <= 64:
                return "55-64"
            else:
                return "65+"
        except:
            return "Unknown"
    
    df_age["AgeGroup"] = df_age["AgeResponse"].apply(group_age)
    
    df_age_grouped = df_age.groupby(["Year", "AgeGroup"])["ResponseCount"].sum().reset_index()
    
    return df_age_grouped

def plot_age_distribution(df_age_grouped):
    age_order = ["Under 18", "18-24", "25-34", "35-44", "45-54", "55-64", "65+"]
    
    plt.figure(figsize=(8, 4))
    ax = sns.barplot(data=df_age_grouped, 
                    x="AgeGroup", 
                    y="ResponseCount", 
                    hue="Year", 
                    palette="Set2", 
                    order=age_order)
    
    plt.yscale("log")
    
    for p in ax.patches:
        if p.get_height() > 0:
            ax.annotate(f'{int(p.get_height())}',
                       (p.get_x() + p.get_width() / 2., p.get_height()),
                       ha='center', va='bottom', fontsize=6, color='black')
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.xlabel("Age Group")
    plt.ylabel("Number of Respondents")
    plt.title("Grouped Age Distribution by Survey Year")
    plt.xticks(rotation=45)
    plt.legend(title="Survey Year")
    
    plt.show()

def get_gender_distribution(conn):
    query = """
    SELECT 
        a.AnswerText AS GenderResponse, 
        COUNT(*) AS ResponseCount
    FROM Answer a
    JOIN Question q ON a.QuestionID = q.QuestionID
    WHERE q.QuestionText = 'What is your gender?'
    GROUP BY a.AnswerText
    ORDER BY ResponseCount DESC;
    """
    
    df_gender = pd.read_sql(query, conn)
    
    def classify_gender(gender):
        gender = gender.lower().strip()  
        if "female" in gender:
            return "Female"
        elif "male" in gender:
            return "Male"
        else:
            return "Other"
    
    
    df_gender["GenderGroup"] = df_gender["GenderResponse"].apply(classify_gender)
    
    df_gender_grouped = df_gender.groupby("GenderGroup")["ResponseCount"].sum().reset_index()
    
    return df_gender_grouped

def plot_gender_distribution(df_gender_grouped):
    with warnings.catch_warnings():
        warnings.simplefilter(action='ignore', category=FutureWarning)
        
        plt.figure(figsize=(6, 4))
        
        ax = sns.barplot(data=df_gender_grouped, 
                        x="GenderGroup", 
                        y="ResponseCount", 
                        order=["Male", "Female", "Other"], 
                        palette="Set2", 
                        legend=False)
        
        
        for p in ax.patches:
            ax.annotate(f'{int(p.get_height())}',
                       (p.get_x() + p.get_width() / 2., p.get_height()),
                       ha='center', va='bottom', fontsize=8, color='black')
        
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        
        plt.xlabel("Gender")
        plt.ylabel("Number of Respondents")
        plt.title("Overall Gender Distribution (Male, Female, Other)")
        plt.xticks(rotation=0)
        
        plt.show()


def get_country_distribution(conn):
    query = """
    SELECT 
        a.AnswerText AS Country, 
        COUNT(*) AS RespondentCount
    FROM Answer a
    JOIN Question q ON a.QuestionID = q.QuestionID
    WHERE q.QuestionText = 'What country do you live in?'
    GROUP BY a.AnswerText
    ORDER BY RespondentCount DESC;
    """
    
    df_country = pd.read_sql(query, conn)
    
    def clean_country(country):
        if country in ["United States of America", "United States"]:
            return "United States"
        else:
            return "Other"
    
    
    df_country["CountryGroup"] = df_country["Country"].apply(clean_country)
    
    
    num_other_countries = df_country[df_country["CountryGroup"] == "Other"]["Country"].nunique()
    
    
    df_country_grouped = df_country.groupby("CountryGroup", as_index=False)["RespondentCount"].sum()
    
 
    df_country_grouped["CountryGroup"] = pd.Categorical(
        df_country_grouped["CountryGroup"], 
        categories=["United States", "Other"], 
        ordered=True
    )
    df_country_grouped = df_country_grouped.sort_values("CountryGroup")
    
    return df_country_grouped, num_other_countries

def plot_country_distribution(df_country_grouped, num_other_countries):
    with warnings.catch_warnings():
        warnings.simplefilter(action='ignore', category=FutureWarning)
        
        plt.figure(figsize=(6, 4))
        
        ax = sns.barplot(data=df_country_grouped, 
                        x="CountryGroup", 
                        y="RespondentCount", 
                        palette="Set2", 
                        order=["United States", "Other"])
        
        
        for p in ax.patches:
            ax.annotate(f'{int(p.get_height())}',
                       (p.get_x() + p.get_width() / 2., p.get_height()),
                       ha='center', va='bottom', fontsize=8, color='black')
        
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        
        plt.xlabel("Country")
        plt.ylabel("Number of Respondents")
        plt.title("Respondents: United States vs. Other")
        plt.xticks(rotation=0, fontsize=10)
        
        
        plt.figtext(0.99, 0.01, 
                   f"'Other' category includes respondents from {num_other_countries} different countries.",
                   ha='right', fontsize=8, style='italic')
        
        plt.tight_layout()
        plt.show()

def get_state_distribution(conn):
    query = """
    SELECT 
        a.AnswerText AS State, 
        COUNT(*) AS RespondentCount
    FROM Answer a
    JOIN Question q ON a.QuestionID = q.QuestionID
    WHERE q.QuestionText = 'If you live in the United States, which state or territory do you live in?'
    GROUP BY a.AnswerText
    ORDER BY RespondentCount DESC;
    """
    
    return pd.read_sql(query, conn)

def plot_state_distribution(df_state):
    with warnings.catch_warnings():
        warnings.simplefilter(action='ignore', category=FutureWarning)
        
        plt.figure(figsize=(10, 4))
        ax = sns.barplot(data=df_state, 
                        x="State", 
                        y="RespondentCount", 
                        palette="Set2")
        

        for p in ax.patches:
            ax.annotate(f'{int(p.get_height())}',
                       (p.get_x() + p.get_width() / 2., p.get_height()),
                       ha='center', va='bottom', fontsize=5.5, color='black')
        
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        
        plt.xlabel("State/Territory")
        plt.ylabel("Number of Respondents")
        plt.title("Distribution of Respondents by US State/Territory")
        plt.xticks(rotation=90, fontsize=5.5)
        
        plt.tight_layout()
        plt.show()

def get_employment_distribution(conn):
    query = """
    SELECT 
        a.UserID,
        a.AnswerText AS SelfEmploymentStatus
    FROM Answer a
    JOIN Question q ON a.QuestionID = q.QuestionID
    WHERE q.QuestionText = 'Are you self-employed?';
    """
    
    df_self_employment = pd.read_sql(query, conn)
    
    def classify_employment(status):
        if status == "-1":
            return "Missing" 
        elif status == "0":
            return "Employee"  
        elif status == "1":
            return "Self-Employed"
        else:
            return "Other"
    
    
    df_self_employment["EmploymentCategory"] = df_self_employment["SelfEmploymentStatus"].apply(classify_employment)
    

    employment_counts = df_self_employment["EmploymentCategory"].value_counts()
    
    return employment_counts

def plot_employment_distribution(employment_counts):
    with warnings.catch_warnings():
        warnings.simplefilter(action='ignore', category=FutureWarning)
        
        plt.figure(figsize=(6, 4))
        ax = sns.barplot(x=employment_counts.index, 
                        y=employment_counts.values, 
                        palette="Set2")
        
        
        for p in ax.patches:
            ax.annotate(f'{int(p.get_height())}',
                       (p.get_x() + p.get_width() / 2., p.get_height()),
                       ha='center', va='bottom', fontsize=10, color='black')
        
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        
        plt.xlabel("Employment Category")
        plt.ylabel("Number of Respondents")
        plt.title("Self-Employed vs. Company Employees")
        plt.xticks(rotation=0)
        
        plt.tight_layout()
        plt.show()

def get_full_survey_data(conn):
    query = """
    SELECT 
        a.UserID,
        a.SurveyID,
        MAX(CASE WHEN q.questionid = 1 THEN a.AnswerText END) AS age,
        MAX(CASE WHEN q.questionid = 2 THEN a.AnswerText END) AS gender,
        MAX(CASE WHEN q.questionid = 3 THEN a.AnswerText END) AS country,
        MAX(CASE WHEN q.questionid = 4 THEN a.AnswerText END) AS us_state,
        MAX(CASE WHEN q.questionid = 5 THEN a.AnswerText END) AS employment,
        MAX(CASE WHEN q.questionid = 33 THEN a.AnswerText END) AS mental_health_disorder,
        MAX(CASE WHEN q.questionid = 10 THEN a.AnswerText END) AS mental_health_benefits,
        MAX(CASE WHEN q.questionid = 56 THEN a.AnswerText END) AS unsupportive_response,
        MAX(CASE WHEN q.questionid = 8 THEN a.AnswerText END) AS company_size,
        MAX(CASE WHEN q.questionid = 11 THEN a.AnswerText END) AS anonymity_protected,
        MAX(CASE WHEN q.questionid = 9 THEN a.AnswerText END) AS tech_company,
        MAX(CASE WHEN q.questionid = 12 THEN a.AnswerText END) AS interview_mental_health,
        MAX(CASE WHEN q.questionid = 115 THEN a.AnswerText END) AS diagnosed_conditions,
        MAX(CASE WHEN q.questionid = 116 THEN a.AnswerText END) AS suspected_conditions,
        MAX(CASE WHEN q.questionid = 91 THEN a.AnswerText END) AS employer_priorities
    FROM Answer a
    JOIN Question q ON a.QuestionID = q.questionid
    WHERE q.questionid IN (1, 2, 3, 4, 5, 33, 10, 56, 8, 11, 9, 12, 115, 116, 91)
    GROUP BY a.UserID, a.SurveyID
    """
    
    return pd.read_sql(query, conn)


def get_company_type_distribution(conn):
    query = """
    SELECT 
        a.AnswerText,
        COUNT(*) as count
    FROM Answer a
    JOIN Question q ON a.QuestionID = q.QuestionID
    WHERE q.QuestionID = 9
    GROUP BY a.AnswerText
    ORDER BY 
        CASE 
            WHEN a.AnswerText = '1' THEN 1
            WHEN a.AnswerText = '0' THEN 2
            WHEN a.AnswerText = '-1' THEN 3
            ELSE 4
        END;
    """
    return pd.read_sql(query, conn)

def plot_company_type_distribution(df_tech_company):
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x='AnswerText', y='count', data=df_tech_company, palette='Set2')

   
    plt.title('Are the employers primarily tech companies/organisations?', 
              pad=20, fontsize=12)
    plt.xlabel('', fontsize=10)
    plt.ylabel('Number of Respondents', fontsize=10)

 
    labels = ['Tech company', 'Non-tech company', 'No response']
    ax.set_xticklabels(labels)

    
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', 
                    (p.get_x() + p.get_width()/2., p.get_height()),
                    ha='center', va='bottom')
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    plt.show()