story = {
  "start" : ["There is a fork in the path in the woods. Left or Right?", ["left", "right"]],
  "left" : ["You encounter a giant monster. Fight or Charm?", ["fight", "charm"]],
  "right" : ["You see a river and a bridge with a troll. Across the river is a way out of the woods! Swim or Troll?", ["swim", "troll"]],
  "fight" : ["Fight the monster? With what?? Your tiny fists? You died. The end.", []],
  "charm" : ["You and the monster have a lot in common! You become best friends. The end.", []],
  "swim" : ["You aren't a very strong swimmer. You drowned. The end.", []],
  "troll" : ["The troll is super laid back and let's you pass. You've made it out of the woods! The end.", []]
}

prevchoice = "start"

while True:
  print(story[prevchoice][0])
  if story[prevchoice][1]:
    nextchoice = input("ur choice:")
    nextchoice = nextchoice.lower()
    while nextchoice not in story[prevchoice][1]:
      print("invalid. try again.")
      nextchoice = input(story[prevchoice][0])
    prevchoice = nextchoice
  else:
    print("Goodbye!")
    break