from seleniumbase import BaseCase


class TestHomePage(BaseCase):
    def test_verify_page_title_and_url(self):
        # open home page
        self.open('https://practice-react.sdetunicorns.com/')

        # assert url and title contains SDET Unicorns
        self.assert_url_contains('sdetunicorns')
        self.assert_title_contains('SDET Unicorns')

# para rodar o teste , basta digitar 'pytest' no terminal

    def test_search_flow(self):
        self.open('https://practice-react.sdetunicorns.com/')

        # click on the search input field
        self.click('.search-active')

        # type lenovo in the search input field
        self.type(selector="[placeholder='Search']", text='Lenovo')

        # click on search button
        self.click('.button-search')

        # assert the text is visible
        self.assert_text_visible('Showing Results for Lenovo')

    def test_search_flow_with_xpath(self):
        self.open('https://practice-react.sdetunicorns.com/')

        # click on the search input field
        self.click("//button[@class='search-active']")

        # type lenovo in the search input field
        self.type(selector="//input[@placeholder='Search']", text='Lenovo')

        # click on search button
        self.click("//button[@class='button-search']")

        # assert the text is visible
        self.assert_text_visible('Showing Results for Lenovo')


    def test_nav_links(self):
    # ^ para rodar apenas uma funcao ->>> pytest -s test_home.py::TestHomePage::test_nav_links
        self.open('https://practice-react.sdetunicorns.com/')
        self.assert_text(text='Products', selector='.main-menu li:nth-child(2)')

        expected_nav_test = ['Home', 'Products', 'About Us', 'Contact', 'Upload']

        for i, text in enumerate(expected_nav_test, start=1):
            # print(i, text)
            self.assert_text(text, selector=f'.main-menu li:nth-child({i})')

