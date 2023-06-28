Feature: Add to cart in amazon.in
  Scenario Outline: Login to amazon.in website and add an item to the shopping cart
    Given User launches Google Chrome web browser
    And User opens www.amazon.in
    When user enters mobile number "<mobileno>"
    And user enters password "<password>"
    #And user logs in successfully
    Then User searches for required item
    And Clicks on the desired item
    And Adds the item to the shopping cart
    And Displays the offers

    Examples:
      | mobileno | password |
      |          |          |
