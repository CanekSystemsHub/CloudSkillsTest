# To run the test
# Invoke-Pester .\PS_test2.ps1

Describe "New-ResourceGroup" {
    $location = 'eastus2'
    $name = 'CanekSystems'
        
    It "Name should be CanekSystems" {
            $name | Should Be 'CanekSystems'
        }
    
    It "location should be eastus2" {
            $location | Should Be 'eastus2'
        }
}