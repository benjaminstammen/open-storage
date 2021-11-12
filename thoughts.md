# client still needs the following features:

## Applets

## Database

File

| uuid | filepath | directory FK | sha |

- How will files be tracked?
    - modifications are easy when file isn't moved
    - moves + renames are detectable
        - might need to lean on some expert tools to do intelligent diffs
- Why a UUID?
    - allows for a resource to be tracked across moves and have a more complete history
Directory
- Directory object allows for a 1:many relationship between directories and files, and makes renames a lot easier to perform.
- Makes sync/no-sync easier to deal with, slightly?

## server client

## multipart upload logic

# server still needs the following features:

## CDK deployment logic