# Convert-Base
Python script to convert any base to any base. the function ten_to_base() can be extended to any base but symbols for each new base must be provided by the use of the user. Support for extention on BaseX to Base10 conversion is limited due to the need for the special characters incompatibily with pythons int() function. This is a future target and will be supported in a later version.

###To use do as follows:
>convert_base(x,original_base,new_base)
>ten_to_base(x,new_base,extend=['!','@','#'])

Note, the list under the extend argument is completely up to the user to define.
