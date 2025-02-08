import openai

def generate_summary(repo_url, code_structure):
    prompt = f"""
    Summarize the following repository:

    - Repository: {repo_url}
    - Files analyzed: {len(code_structure)}

    Here's an overview of the code structure:
    {code_structure[:3]}

    Explain the main points of the repository and the overall hierarchy in a succint way.set
    """

    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role":"system", "content":"You are a code summarizer"},
                  {"role":"user", "content":prompt}]
    )

    return response["choices"][0]["message"]["content"]
