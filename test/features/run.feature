Feature: Asterix runs

  Scenario: running
    Given the terrain is fine
    When asterix runs "10"
    Then the terray is a bit messy
