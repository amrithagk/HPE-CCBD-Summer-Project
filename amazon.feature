Feature: Login to Amazon e commerce and product purchase

    Scenario: Get price, description, and offers for a specific TV
    
      Given I launch Chrome browser
      When I visit amazon website
      And Amazon homepage is opened successfully
    
      
      And I log in with valid phone number or email "<mobileno>" and password "<password>"
      Then I should login successfully
    
    
    
    Examples:
        |7019522431|Nisarga@123

