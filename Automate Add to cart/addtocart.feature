Feature: Automatically login to e-commerce website and add an item to the shopping cart
  Scenario: Add to cart in amazon.in
    Given User opens www.amazon.in
    And user logs in to their account successfully
    When User searches for required item
    And Clicks on the desired item
    Then Add the item to the shopping cart