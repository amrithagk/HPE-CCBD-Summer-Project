Feature: Login to Amazon e commerce and product purchase

Scenario: Get price, description, and offers for a specific TV

  Given I launch Chrome browser
  When I visit amazon website
  Then Amazon homepage is opened successfully

  Given I am on the Amazon e-commerce site
  When I log in with valid phone number or email "9449247161" and password "Suma@1980"
  And I search for "SONY 55inch TV"
  Then I should see the "SONY 55inch TV" listed in the 3rd position

  When I click on the "SONY 55inch TV"
  Then I should be redirected to the product page
  
    And the user navigates to the reviews section
    Then the user should be able to view the reviews
