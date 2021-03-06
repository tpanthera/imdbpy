def test_search_company_should_list_default_number_of_companies(ia):
    companies = ia.search_company('pixar')
    assert len(companies) == 20


def test_search_company_limited_should_list_requested_number_of_companies(ia):
    companies = ia.search_company('pixar', results=7)
    assert len(companies) == 7


def test_search_company_unlimited_should_list_correct_number_of_companies(ia):
    companies = ia.search_company('pixar', results=500)
    assert 35 <= len(companies) <= 50


def test_search_company_too_many_should_list_upper_limit_of_companies(ia):
    companies = ia.search_company('pictures', results=500)
    assert len(companies) == 200


def test_search_company_if_none_result_should_be_empty(ia):
    companies = ia.search_company('%e3%82%a2')
    assert companies == []
