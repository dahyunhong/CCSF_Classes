{\rtf1\ansi\ansicpg1252\cocoartf2511
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red154\green154\blue154;\red255\green255\blue254;\red0\green0\blue0;
\red0\green0\blue255;\red144\green1\blue18;\red19\green120\blue72;}
{\*\expandedcolortbl;;\cssrgb\c66667\c66667\c66667;\cssrgb\c100000\c100000\c99608;\cssrgb\c0\c0\c0;
\cssrgb\c0\c0\c100000;\cssrgb\c63922\c8235\c8235;\cssrgb\c3529\c53333\c35294;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl420\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # Write a Python program preference.py to (2 points):-\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Ask the user \'91How much do you like pizza on a scale of 1 (hate) to 5 (love)?\'92\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Ask the user \'91How much do you like tacos on a scale of 1 (hate) to 5 (love)?\'92\cf4 \cb1 \strokec4 \
\
\cf2 \cb3 \strokec2 # If users like pizza more than tacos print \'91You like pizzas more than tacos\'92. (You do not need an else condition)\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\sl420\partightenfactor0
\cf4 \cb3 pizza =\cf5 \strokec5 int\cf4 \strokec4 (\cf5 \strokec5 input\cf4 \strokec4 (\cf6 \strokec6 "How much do you like pizza on a scale of 1 (hate) to 5 (love)?"\cf4 \strokec4 ))\cb1 \
\pard\pardeftab720\sl420\partightenfactor0
\cf5 \cb3 \strokec5 while\cf4 \strokec4 (pizza<\cf7 \strokec7 1\cf4 \strokec4  \cf5 \strokec5 or\cf4 \strokec4  pizza>\cf7 \strokec7 5\cf4 \strokec4 ):\cb1 \
\pard\pardeftab720\sl420\partightenfactor0
\cf4 \cb3   pizza = \cf5 \strokec5 int\cf4 \strokec4 (\cf5 \strokec5 input\cf4 \strokec4 (\cf6 \strokec6 "How much do you like pizza on a scale of 1 (hate) to 5 (love)?"\cf4 \strokec4 ))\cb1 \
\
\cb3 tacos =\cf5 \strokec5 int\cf4 \strokec4 (\cf5 \strokec5 input\cf4 \strokec4 (\cf6 \strokec6 "How much do you like tacos on a scale of 1 (hate) to 5 (love)?"\cf4 \strokec4 ))\cb1 \
\pard\pardeftab720\sl420\partightenfactor0
\cf5 \cb3 \strokec5 while\cf4 \strokec4 (tacos <\cf7 \strokec7 1\cf4 \strokec4  \cf5 \strokec5 or\cf4 \strokec4  tacos > \cf7 \strokec7 5\cf4 \strokec4 ):\cb1 \
\pard\pardeftab720\sl420\partightenfactor0
\cf4 \cb3   tacos = \cf5 \strokec5 int\cf4 \strokec4 (\cf5 \strokec5 input\cf4 \strokec4 (\cf6 \strokec6 "How much do you like tacos on a scale of 1 (hate) to 5 (love)?"\cf4 \strokec4 ))\cb1 \
\
\
\pard\pardeftab720\sl420\partightenfactor0
\cf5 \cb3 \strokec5 if\cf4 \strokec4  (pizza > tacos):\cb1 \
\pard\pardeftab720\sl420\partightenfactor0
\cf4 \cb3   \cf5 \strokec5 print\cf4 \strokec4 (\cf6 \strokec6 "You like pizzas more than tacos"\cf4 \strokec4 )\cb1 \
\
}