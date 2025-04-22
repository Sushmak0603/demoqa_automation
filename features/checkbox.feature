Feature: Checkbox Tree testing

  Background:
    Given the user has launched the DEMOQA application
    And the user click on "Elements" card
    Then the user should be navigated to a URL containing "demoqa.com/elements"
    Then the menu list for "Elements" should be expanded
    Then the menu list items for "Elements" should be
      |Items                   |
      |Text Box                |
      | Check Box              |
      | Radio Button           |
      | Web Tables             |
      | Buttons                |
      | Links                  |
      | Broken Links - Images  |
      | Upload and Download    |
      | Dynamic Properties     |
    Then the user navigates to "Check Box" section under "Elements"
    Then the user should be navigated to a URL containing "demoqa.com/checkbox"
    Then the user should be able to see "Home" in the tree node

  Scenario: Dynamically expand the tree at all levels (TC001)
    Then the user expands the tree at all levels - through expand all (+) button

  Scenario: Tick any parent node and dynamically assert that all nested elements have correct icons (TC002)
    Then the user expands the tree at all levels - through code
    Then the user ticks "WorkSpace" parent node in the tree
    Then verify if all the descendants of the selected parent node are fully-ticked automatically
    Then verify if all the ancestors of the selected parent node are half-ticked and fully-ticked accordingly




