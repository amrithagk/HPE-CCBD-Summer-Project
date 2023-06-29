Feature: Search for a product on amazon
  Scenario:Search for the search bar
    Given launch chrome browser
    When open amazon home page
    And search for the "SONY 55inch TV"
    And click on search button
    And find the third product
    And fetch price of the product
    And fetch the description of product
    And click add to cart button
    And close browser
