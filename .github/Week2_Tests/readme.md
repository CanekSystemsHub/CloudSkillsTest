# WEEK'S 2 SCRIPTS ON CLOUDSKILLS BOOTCAMP
The purpose of this bootcamp's weeks scripts is to show how does the Testing and linting work on both Poweshell and Python Frameworks

## STATUS WIP
The code found on this sections is currently in Work in progress and the readme will be be updated accordinly

## PowerShell code
The PoweShell code is for creating a Resource Group in Azure

## How to use the PowherShell code
The New-ResourceGroup Function is found in the PS_Test1ps1 file  in the root directory and can be used as a reusable function.
the user has the ability to pass in parameters at runtime to ensure they can re-use script at any point for any environment.

## Python code
The Python code is for creating a S3 Bucket in AWS

## How to use Python Code
Pending to update

## Powershell Example
```
function New-ResourceGroup{
    [cmdletbinding(SupportsShouldProcess)]

    param (
        [parameter(Mandatory)]
        [string]$rgName,

        [parameter(Mandatory)]
        [string]$location
    )

    $params =@{
    'Name' = $rgName
    'Location' = $location
    }

    if ($pscmdlet.ShouldProcess('location')){
        New-AzResourceGroup @params
    }
 }
 ```

 ## Python Examples
 ```
import boto3
import sys

try:
    def main():
        create_s3bucket(bucket_name)

except Exception as e:
    print(e)

def create_s3bucket(bucket_name):
    s3_bucket=boto3.client(
        's3',
    )

    bucket = s3_bucket.create_bucket(
        Bucket=bucket_name,
        ACL='private',
    )

    print(bucket)

bucket_name = sys.argv[1]

if __name__ == '__main__':
    main()

 ```

 ## Testing
Both Pwersshell and Python code have unit tests available to ensure that the desired outcomes, including values and types are accurate.
Such test can be found a the root directory of Week2.

## Contributors
INITIAL Victor Jimenez