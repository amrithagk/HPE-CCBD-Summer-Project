Feature: Login to Amazon e commerce and product purchase

Scenario: Get price, description, and offers for a specific TV

  Given I launch Chrome browser
  When I visit amazon website
  Then Amazon homepage is opened successfully

  Given I am on the Amazon e-commerce site
  When I log in with valid phone number or email "9449247161" and password "Suma@1980"
  
  
    And the user navigates to the reviews section
    Then the user should be able to view the reviews
