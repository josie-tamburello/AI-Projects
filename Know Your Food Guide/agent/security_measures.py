Use defensive prompts: Explicitly instruct the model to treat retrieved context as data
only and to ignore any instructions within it. The prompts in this tutorial include such
instructions.

2. Wrap context with delimiters: Use clear structural markers (e.g., XML tags
like <context>...</context> ) to separate retrieved data from instructions, making it easier for the model to distinguish between them.

3. Validate responses: Check that the model’s output matches the expected format (e.g.,
plain text) and handle unexpected formats gracefully.