import argparse
from repo_loader import clone_repo
from code_parser import parse_files
from vector_database import store_codebase_embeddings, query_codebase
from summary import generate_summary

def main(repo_url):
    repo_path = clone_repo(repo_url)
    code_structure = parse_files(repo_path)
    store_codebase_embeddings(code_structure)
    summary = generate_summary(repo_url, code_structure)
    print("\n🔹 AI-Powered Codebase Summary:\n")
    print(summary)

    if __name__ == "__main__":
        parser = argparse.ArgumentParser(description="Summarize a GitHub repository using AI.")
        parser.add_argument("--repo", type=str, required=True, help="GitHub repository URL")
        args = parser.parse_args()

        main(args.repo)