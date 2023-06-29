Feature: Login to Amazon e commerce and product purchase

  Scenario: Get price, description, and offers for a specific TV
  
    Given I launch Chrome browser
    When I visit amazon website
    And Amazon homepage is opened successfully
  
    And I am on the Amazon e-commerce site
    And I log in with valid phone number or email "<mobileno>" and password "<password>"
    And I should login successfully
  
    And search for the "SONY 55inch TV"
    And click on search button
    Then find the third product
    Then fetch price of the product
    Then fetch the description of product
    Then click add to cart button
  
    And Displays the offers
      
    And the user navigates to the reviews section
    Then the user should be able to view the reviews
  
    

  Examples:
      | mobileno | password |
      |          |          |
  

