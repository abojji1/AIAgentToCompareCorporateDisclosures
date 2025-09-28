from bs4 import BeautifulSoup
import requests
USER_AGENT = "your-email@example.com (SEC Filing Compare Agent)"

def extract_sections_from_html(html: str):
    soup = BeautifulSoup(html, "html.parser")
    sections = {}
    for header in soup.find_all(['h1','h2','h3','b','strong']):
        text = header.get_text(separator=' ', strip=True).lower()
        if 'management' in text and 'discussion' in text or 'md&a' in text:
            sections.setdefault('MD&A', '')
            content = []
            for sib in header.find_next_siblings():
                if sib.name and sib.name.startswith('h'):
                    break
                content.append(sib.get_text(' ', strip=True))
                if len(' '.join(content)) > 8000:
                    break
            sections['MD&A'] = sections['MD&A'] + '\n' + ' '.join(content)
        if 'risk' in text and 'factor' in text:
            sections.setdefault('Risk Factors', '')
            content = []
            for sib in header.find_next_siblings():
                if sib.name and sib.name.startswith('h'):
                    break
                content.append(sib.get_text(' ', strip=True))
                if len(' '.join(content)) > 8000:
                    break
            sections['Risk Factors'] = sections['Risk Factors'] + '\n' + ' '.join(content)
    return sections

def fetch_xbrl_companyfacts(cik: str):
    url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{int(cik):010d}.json"
    r = requests.get(url, headers={"User-Agent": USER_AGENT})
    r.raise_for_status()
    return r.json()
