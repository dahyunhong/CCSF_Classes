{\rtf1\ansi\ansicpg1252\cocoartf2511
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue255;\red255\green255\blue254;\red0\green0\blue0;
\red19\green120\blue72;\red144\green1\blue18;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c100000;\cssrgb\c100000\c100000\c99608;\cssrgb\c0\c0\c0;
\cssrgb\c3529\c53333\c35294;\cssrgb\c63922\c8235\c8235;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl420\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import\cf4 \strokec4  random\cb1 \
\
\pard\pardeftab720\sl420\partightenfactor0
\cf4 \cb3 RandomNumber = random.randint(\cf5 \strokec5 1\cf4 \strokec4 ,\cf5 \strokec5 20\cf4 \strokec4 ) \cb1 \
\
\
\cb3 Guess = \cf2 \strokec2 int\cf4 \strokec4 (\cf2 \strokec2 input\cf4 \strokec4 (\cf6 \strokec6 "Guess the number: "\cf4 \strokec4 ))\cb1 \
\
\pard\pardeftab720\sl420\partightenfactor0
\cf2 \cb3 \strokec2 while\cf4 \strokec4  Guess != RandomNumber:\cb1 \
\pard\pardeftab720\sl420\partightenfactor0
\cf4 \cb3 \'a0\'a0\cf2 \strokec2 if\cf4 \strokec4  (Guess < RandomNumber):\cb1 \
\cb3 \'a0\'a0\'a0\'a0\cf2 \strokec2 print\cf4 \strokec4 (\cf6 \strokec6 "Too low!"\cf4 \strokec4 )\cb1 \
\cb3 \'a0\'a0\'a0\'a0Guess =  \cf2 \strokec2 int\cf4 \strokec4 (\cf2 \strokec2 input\cf4 \strokec4 (\cf6 \strokec6 "Guess the number: "\cf4 \strokec4 )) \cb1 \
\cb3 \'a0\'a0\cf2 \strokec2 else\cf4 \strokec4 :\cb1 \
\cb3 \'a0\'a0\'a0\'a0\cf2 \strokec2 print\cf4 \strokec4 (\cf6 \strokec6 "Too high!"\cf4 \strokec4 )\cb1 \
\cb3 \'a0\'a0\'a0\'a0Guess =  \cf2 \strokec2 int\cf4 \strokec4 (\cf2 \strokec2 input\cf4 \strokec4 (\cf6 \strokec6 "Guess the number: "\cf4 \strokec4 ))\cb1 \
\
\pard\pardeftab720\sl420\partightenfactor0
\cf2 \cb3 \strokec2 print\cf4 \strokec4 (\cf6 \strokec6 "You got it!"\cf4 \strokec4 )\cb1 \
\
}