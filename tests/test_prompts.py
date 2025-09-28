from src.my_agent.prompts import COMPARE_TEMPLATE

def test_template_has_placeholders():
    assert '{section}' in COMPARE_TEMPLATE
