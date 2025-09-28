import requests
USER_AGENT = "your-email@example.com (SEC Filing Compare Agent)"

def get_filing_document_url(cik: str, accession: str):
    acc_no = accession.replace('-', '')
    return f"https://www.sec.gov/ix?doc=/Archives/edgar/data/{int(cik)}/{acc_no}/xbrl.htm"

def download_filing_html(cik: str, accession: str) -> str:
    url = get_filing_document_url(cik, accession)
    r = requests.get(url, headers={"User-Agent": USER_AGENT})
    r.raise_for_status()
    return r.text
