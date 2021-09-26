#!/bin/bash

# Prints simple instructions
instructions(){
printf "THE BEST TIC TAC TOE GAME\n"
printf "KEY IN THE VALUE 0 TO 8 WHEN ITS YOUR MOVE\n"
printf "\n"
printf "0 | 1 | 2\n"
printf '%.s-' {1..10}
printf "\n"
printf "3 | 4 | 5\n"
printf '%.s-' {1..10}
printf "\n"
printf "6 | 7 | 8\n"
printf "\n"
}

# Sets opponent's move
opponent(){
OPPONENT=$(( $RANDOM % 9 ))
while ! [ ${TTC[$OPPONENT]} == "." ]
do
	OPPONENT=$(( $RANDOM % 9 ))
done
TTC[$OPPONENT]="O"
}

# Prints board with fresh and updated moves
print_board(){
printf "${TTC[0]} | ${TTC[1]} | ${TTC[2]}\n"
printf '%.s-' {1..10}
printf "\n"
printf "${TTC[3]} | ${TTC[4]} | ${TTC[5]}\n"
printf '%.s-' {1..10}
printf "\n"
printf "${TTC[6]} | ${TTC[7]} | ${TTC[8]}\n"
printf "\n"
}

# Ask user for move
ask_move(){
printf "YOUR MOVE:\n"
read -r MOVE
printf "\n"
}

# Ensure move is valid and sets move and place
# Tile in the board
user_move(){
ask_move
while ! [[ $MOVE =~ ^[0-8]$ ]]
do
	printf "INVALID MOVE\n\n"
	ask_move
done

while ! [ ${TTC[$MOVE]} == "." ]
do
	printf "POSITION TAKEN\n\n"
	ask_move
done

TTC[$MOVE]="X"
printf "\n"
}

# Check if matches
match_three(){
if [ ${TTC[$1]} == ${TTC[$2]} ] && [ ${TTC[$2]} == ${TTC[$3]} ] && [ ${TTC[$1]} != "." ]
then 
END=1
WINNER=${TTC[$1]}
fi
}

# Algo to check all possible winning configs
# Leaves if any winner, or no more tile to be placed
winner_checker(){
  match_three 0 1 2
  match_three 3 4 5
  match_three 6 7 8
  
  match_three 0 4 8
  match_three 2 4 6
   
  match_three 0 3 6
  match_three 1 4 7
  match_three 2 5 8
  
  if [ $END == 1 ]
  then
  print_board
  printf "END OF GAME\n"
  printf "THE WINNER IS $WINNER\n"
  exit 0
  fi
  
  ((COUNT++))
  if [ $COUNT == 9 ]
  then
  print_board
  printf "END OF GAME\n"
  printf "THE WINNER IS NO ONE\n"
  exit 0
  fi
}

# Kinda like my main
TTC=(. . . . . . . . .)
END=0
COUNT=0
while true
do
	clear
	instructions
	print_board
	user_move
	winner_checker
	opponent
	winner_checker
done

