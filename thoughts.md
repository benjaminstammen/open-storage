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

## APIs

### Request

- start_upload
    - mapped_name (encrypted with password or some other private key)
    - filesize
    - last_modified
    - known_checksums (allows server to eventually verify that the file was successfully uploaded)
        - B2 supplies SHA1
        - S3 supplies MD5
        - The above are "bad", but these are being used for file integrity purposes, not passwords. Not worried about it.

### Response

- start_updated
    - presigned_uri_list
    - 


## CDK deployment logic

# etc

object stores don't generally support partial updates of uploaded objects. This seems to suggest that in order to get partial updates to work, there will have to be
some splintering of objects into minimally-sized chunks that can then be updated as needed (e.g. a 2GB file in 4MB chunks could have an edited section updated)