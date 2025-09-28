import os
from argparse import ArgumentParser
from src.my_agent.compare import compare_filings

def main():
    parser = ArgumentParser()
    parser.add_argument("--cik-a", required=True)
    parser.add_argument("--accession-a", required=True)
    parser.add_argument("--cik-b", required=True)
    parser.add_argument("--accession-b", required=True)
    parser.add_argument("--section", default="MD&A")
    args = parser.parse_args()
    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("Please set OPENAI_API_KEY in environment")
    out = compare_filings({"cik": args.cik_a, "accession": args.accession_a, "id": "A"}, {"cik": args.cik_b, "accession": args.accession_b, "id": "B"}, section=args.section)
    print(out)

if __name__ == '__main__':
    main()
