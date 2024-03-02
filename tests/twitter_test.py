""" twitter_test.py """

import pytest

@pytest.fixture
def cat_link_twit():
    return "https://twitter.com/CatsIX/status/1763785244044374107"

@pytest.fixture
def cat_link_x():
    return "https://x.com/CatsIX/status/1763785244044374107"

def test_fix_twitter_link(cat_link_twit):
    if "https://twitter.com/" in cat_link_twit:
        modified_url = "https://fxtwitter.com/"
        new_content = cat_link_twit.replace("https://twitter.com/", modified_url)
        
        assert new_content == "https://fxtwitter.com/CatsIX/status/1763785244044374107"

def test_fix_x_link(cat_link_x):
    if "https://twitter.com/" in cat_link_x:
        modified_url = "https://fxtwitter.com/"
        new_content = cat_link_twit.replace("https://twitter.com/", modified_url)
    
        assert new_content == "https://fixupx.com/CatsIX/status/1763785244044374107"
