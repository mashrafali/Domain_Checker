#!/bin/bash


POST=$QUERY_STRING
DIN=$(echo $POST | cut -d '=' -f 2 | cut -d '&' -f 1)

# Fetching DATA

echo "Content-type: text/html"
echo ""
echo "<html><head><title>Domain Checker"
echo '</title></head><body background="res.jpg">'
echo ""
echo "<h1> NOOR Domain Checker </h1>"
echo "<h2>Domain: $DIN </h2>"
echo "<h3>------------------------------------------------------------------------------------------</h3>"
################################################################################## Running TEST script
############################################
# CUSTOMER DOMAIN CHECKER BY MASHRAF
############################################

# Reading data

CDOMAIN=$DIN

if [ -z "$CDOMAIN" ]                    # Terminate if no input
  then
   echo; echo "Please Provide a customer Domain Name!"
   echo
   kill $$
fi  

if [ "$CDOMAIN" == "noor.net" ]                    # Terminate if its a joke!
  then
   echo; echo "The Tool will not waste it's resources for this, This tool is to test CUSTOMERS Domain Names."
   echo
   kill $$
fi

if [ "$CDOMAIN" == "noorgroup.net" ]                    # Terminate if its a joke!
  then
   echo; echo "The Tool will not waste it's resources for this, This tool is to test CUSTOMERS Domain Names."
   echo
   kill $$
fi


# Clearing new report

echo > report
echo "<pre> ####################################################################################### </pre>"  >> report
echo "<pre> Full Tests Report: </pre>"                        >> report
echo "<pre> ####################################################################################### </pre>"  >> report
# Starting tests:

echo
echo "<h3> Checking Status for Domain: $CDOMAIN </h3>"
echo "<h3> -- </h3>"
echo


################################################## TEST 1 [DNS]:
echo
echo -n " <h3> Test 1 : Customer is DNS Hosted at NOOR  :"
nslookup -q=ns $CDOMAIN 8.8.8.8 > verify.tmp

A1=$(cat verify.tmp | grep -i "nameserver = " |grep -i dns0.noor.net | wc -l)
A2=$(cat verify.tmp | grep -i "nameserver = " |grep -i dns1.noor.net | wc -l)
A3=$(cat verify.tmp | grep -i "nameserver = " |grep -i ns1.noor.com | wc -l)
A4=$(cat verify.tmp | grep -i "nameserver = " |grep -i ns2.noor.com | wc -l)


if [ "$A1" -ge "1" ] 
  then
   check1=ok
   echo "<pre> Customer IS DNS Hosted @NOOR   : Found at dns0.noor.net </pre>"  >> report
   result1="Public Hosted"
fi

if [ "$A1" -ge "1" ]                                           
  then
   check2=ok
   echo "<pre> Customer IS DNS Hosted @NOOR   : Found at dns1.noor.net </pre>"  >> report
   result1="Public Hosted"
fi

if [ "$A3" -ge "1" ]                                           
  then
   check3=ok
   echo "<pre> Customer IS DNS Hosted @NOOR   : Found at ns1.noor.com </pre>"  >> report
   result1="Shared Hosted"
fi

if [ "$A3" -ge "1" ]                                           
  then
   check4=ok
   echo "<pre> Customer IS DNS Hosted @NOOR   : Found at ns2.noor.com </pre>"  >> report 
   result1="Shared Hosted"
fi



if [ -n "$check1" ] || [ -n "$check2" ] || [ -n "$check3" ] || [ -n "$check4" ]
  then
   echo "    YES ($result1) </h3>"
  else
   echo "    NO </h3>"
   echo "<pre> NO DNS Hosting Record Found For This Domain </pre>"  >> report
fi  

################################################### TEST 2 [MAIL]
echo
echo -n " <h3> Test 2 : Customer is Mail Hosted at NOOR :"
nslookup -q=mx $CDOMAIN 8.8.8.8 > verify.tmp

B1=$(cat verify.tmp | grep -i "mail exchanger = " | grep -i mail.noor.com | wc -l)
B2=$(cat verify.tmp | grep -i "mail exchanger = " | grep -i mail3.noor.com | wc -l)
if [ "$B1" -ge "1" ] 
  then
   check5=ok
   echo "<pre> Customer IS MAIL Hosted @NOOR  : Found at mail.noor.com </pre>"  >> report
   result2="Shared Hosted"
fi

if [ "$B2" -ge "1" ]                                           
  then
   check6=ok
   echo "<pre> Customer IS MAIL Hosted @NOOR  : Found at mail3.noor.com </pre>"  >> report
   result2="Shared Hosted"
fi


if [ -n "$check5" ] || [ -n "$check6" ]
  then
   echo "    YES ($result2) </h3>"
  else
   nslookup -q=mx $CDOMAIN 8.8.8.8 | grep -i "mail exchanger =" | cut -d" " -f5 > ListQ.tmp
   while read listQ
    do
        if [ "$listQ" == "mail.noor.net." ]
          then
             continue
        fi
        nslookup -q=a $listQ 8.8.8.8 > verify.tmp
        B3=$(cat verify.tmp | grep -i "41.187.100."  | wc -l)
        B4=$(cat verify.tmp | grep -i "41.187.101."  | wc -l)
        B5=$(cat verify.tmp | grep -i "217.139.226." | wc -l)
        B6=$(cat verify.tmp | grep -i "217.139.227." | wc -l)

       if [ "$B3" -ge "1" ]
         then
          check7=ok
          echo "<pre> Customer IS MAIL Hosted @NOOR  : Found at range 41.187.100.x </pre>"  >> report
          result2="NOOR Hosted"
       fi
       if [ "$B4" -ge "1" ]
         then
          check8=ok
          echo "<pre> Customer IS MAIL Hosted @NOOR  : Found at range 41.187.101.x </pre>"  >> report
          result2="NOOR Hosted"  
       fi
       if [ "$B5" -ge "1" ]
         then
          check9=ok
          echo "<pre> Customer IS MAIL Hosted @NOOR  : Found at range 217.139.226.x </pre>"  >> report
          result2="NOOR Hosted"  
       fi
       if [ "$B6" -ge "1" ]
         then
          check10=ok
          echo "<pre> Customer IS MAIL Hosted @NOOR  : Found at range 217.139.227.x </pre>"  >> report
          result2="NOOR Hosted"  
       fi
       if [ -n "$check7" ] || [ -n "$check8" ] || [ -n "$check9" ] || [ -n "$check10" ]
       then
         echo "    YES ($result2) </h3>"
       else
         Tcheck="fail"
         #echo "    NO </h3>"
         #echo "<pre> NO MAIL Hosting Record Found For This Domain </pre>"  >> report
       fi
    done < ListQ.tmp
    if [ "$Tcheck" == "fail" ] 
     then   
      echo "    NO </h3>"
    fi
fi  

################################################### TEST 3 [WEB]
echo
echo -n "<h3> Test 3 : Customer is WEB Hosted at NOOR  :"
nslookup -q=a www.$CDOMAIN 8.8.8.8 > verify.tmp

C1=$(cat verify.tmp | grep -i "41.187.100."  | wc -l)
C2=$(cat verify.tmp | grep -i "41.187.101."  | wc -l)
C3=$(cat verify.tmp | grep -i "217.139.226." | wc -l)
C4=$(cat verify.tmp | grep -i "217.139.227." | wc -l)


if [ "$C1" -ge "1" ]
  then
   check11=ok
   echo "<pre> Customer IS WEB Hosted @NOOR   : Found at range 41.187.100.x </pre>"  >> report
   result3="Range 100"
fi
if [ "$C2" -ge "1" ]
  then
   check12=ok
   echo "<pre> Customer IS WEB Hosted @NOOR   : Found at range 41.187.101.x </pre>"  >> report
   result3="Range 101"  
fi
if [ "$C3" -ge "1" ]
  then
   check13=ok
   echo "<pre> Customer IS WEB Hosted @NOOR   : Found at range 217.139.226.x </pre>"  >> report
   result3="Range 226"  
fi
if [ "$C4" -ge "1" ]
  then
   check14=ok
   echo "<pre> Customer IS WEB Hosted @NOOR   : Found at range 217.139.227.x </pre>"  >> report
   result3="Range 227"  
fi
if [ -n "$check11" ] || [ -n "$check12" ] || [ -n "$check13" ] || [ -n "$check14" ]
then
  echo "    YES ($result3) </h3>"
else
  echo "    NO </h3>"
  echo "<pre> NO WEB Hosting Record Found For This Domain </pre>"  >> report  
fi

################################################### TEST 4 [Queing]
echo
echo -n " <h3> Test 4 : Is Using NOOR's Queuing Service :"
nslookup -q=mx $CDOMAIN 8.8.8.8 | grep -i "mail exchanger =" | cut -d" " -f5 > verify.tmp
count=$(cat verify.tmp | wc -l)

if [ "$count" -ge "2" ]
   then
     D1=$(cat verify.tmp | grep -i "mail.noor.net"  | wc -l)
     if [ "$D1" -ge "1" ]
       then
        check15=ok
        echo "<pre> Customer Using Queuing Service : mail.noor.net found within preference alongside others </pre>"  >> report
        result4="Service is preferenced"
        echo "    YES ($result4) </h3>"
       else
        echo "    NO </h3>"
        echo "<pre> NO Record For Queuing Service Found For This Domain </pre>"  >> report 
     fi
    else
     echo "    NO </h3>"
     echo "<pre> NO Record For Queuing Service Found For This Domain </pre>"  >> report 
fi

################################################################## End of Tests
echo
echo


################################ Reporting results
echo "<h3> -- </h3>"

#echo " <pre> TESTING FORMAT FONT </pre>"

cat report 

echo
echo


# The End...


