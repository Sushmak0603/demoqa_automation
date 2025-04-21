Feature: Practice Forms Testing

  Background:
    Given the user has launched the DEMOQA application
    And the user click on "Forms" card
#    Then the user should be navigated to a URL containing "demoqa.com/forms"
#    Then the menu list for "Forms" should be expanded
#    Then the menu list items for "Forms" should be
#      |Items                |
#      |Practice Form        |
    Then the user navigates to "Practice Form" section under "Forms"
#    Then the user should be navigated to a URL containing "demoqa.com/automation-practice-form"


#    Scenario: Verify if the Form does not get submitted when no field is entered
#      When the user clicks on "Submit" button
#      Then the field "First Name" should indicate error with "border-color" red
#      Then the field "Last Name" should indicate error with "border-color" red
#      Then the field options for Gender should indicate error with "color" red
#      Then the field "Mobile Number" should indicate error with "border-color" red


#    Scenario: Verify the Mobile Number field accept only numbers, of 10 digits
#      When the user enters "Sushma" in "First Name" field
#      When the user enters "K" in "Last Name" field
#      When the user selects "Female" gender radio button
#      When the user enters "1" in "Mobile Number" field
#      When the user clicks on "Submit" button
#      Then the field "Mobile Number" should indicate error with "border-color" red
#      When the user enters "1234" in "Mobile Number" field
#      When the user clicks on "Submit" button
#      Then the field "Mobile Number" should indicate error with "border-color" red
#      When the user enters "abcdefghik" in "Mobile Number" field
#      When the user clicks on "Submit" button
#      Then the field "Mobile Number" should indicate error with "border-color" red
#      When the user enters "123***$#@&" in "Mobile Number" field
#      When the user clicks on "Submit" button
#      Then the field "Mobile Number" should indicate error with "border-color" red
#      When the user enters "123456789112345" in "Mobile Number" field
#      Then verify if the "Mobile Number" field has accepted only "10" digits
#      When the user enters "1234567890" in "Mobile Number" field
#      When the user clicks on "Submit" button
#      Then the form should be submitted with message "Thanks for submitting the form"
#
  Scenario: Verify the Email field accept only valid email-ids
        When the user enters "Sushma" in "First Name" field
        When the user enters "K" in "Last Name" field
        When the user selects "Female" gender radio button
        When the user enters "1234567890" in "Mobile Number" field
        When the user enters "abc" in "Email" field
        When the user clicks on "Submit" button
        Then the field "Email" should indicate error with "border-color" red
        When the user enters "abc@" in "Email" field
        When the user clicks on "Submit" button
        Then the field "Email" should indicate error with "border-color" red
        When the user enters "abc@gmail" in "Email" field
        When the user clicks on "Submit" button
        Then the field "Email" should indicate error with "border-color" red
        When the user enters "*****@gmail.com" in "Email" field
        When the user clicks on "Submit" button
        Then the field "Email" should indicate error with "border-color" red
        When the user enters "abc@gmail.com" in "Email" field
        When the user clicks on "Submit" button
        Then the form should be submitted with message "Thanks for submitting the form"



