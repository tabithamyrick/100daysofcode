print(r"""\
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'

 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|


""")
gameOver = False
while (gameOver == False):
# First Path trail or forest
    firstChoice = input(r"""
====================================================================================   
Welcome to Treasuer Island, the lost gold is yours if you can survive!
You see a trail along the beach and a forrest in the distance, which way do you go?
====================================================================================

""")

    if(firstChoice != "trail"):
        print(r"""
        
                            _.--....
                 _....---;:'::' ^__/
               .' `'`___....---=-'`
              /::' (`
              \'   `:.
               `\::.  ';-"":::-._  {}
            _.--'`\:' .'`-.`'`.' `{I}
         .-' `' .;;`\::.   '. _: {-I}`\
       .'  .:.  `:: _):::  _;' `{=I}.:|
      /.  ::::`":::` ':'.-'`':. {_I}::/
      |:. ':'  :::::  .':'`:. `'|':|:'
       \:   .:. ''' .:| .:, _:./':.|
    jgs '--.:::...---'\:'.:`':`':./
                       '-::..:::-'

While walking through the forrest you steped on a weird stick, but it wasnt a stick...
You Died....""")
        gameOver = True
        break
# Second Path mountain or stream
    seccondChoice = input(r"""
=================================================================================        
You come to the end of the path. There is a stream runniing away from a mountain. 
Do you swim across the stream to the other side or climb the mounntain?
=================================================================================

""")

    if(seccondChoice != "mountain"):
        print(r"""

          ,---,
  _    _,-'    `--,
 ( `-,'            `\
  \           ,    o \
  /   ,       ;       \
 (_,-' \       `, _  ""/
     pb `-,___ =='__,-'

Oh No its a School of Piranha......
You Died.....""")
        gameOver = True
        break

# Third Path cave left or right
    thirdChoice = input(r"""
============================================================================================
You get to a break in the mountain and find a cave to duck into.
Inside the cave there are two chambers to the left and right, which way should you explore?
=============================================================================================

""")

    if(thirdChoice != "left"):
        print(r"""
 .'"'.        ___,,,___        .'``.
: (\  `."'"```         ```"'"-'  /) ;
 :  \                         `./  .'
  `.                            :.'
    /        _         _        \
   |         0}       {0         |
   |         /         \         |
   |        /           \        |
   |       /             \       |
    \     |      .-.      |     /
     `.   | . . /   \ . . |   .'
 jgs   `-._\.'.(     ).'./_.-'
           `\'  `._.'  '/'
             `. --'-- .'
               `-...-'

You Ran into a Mother Grizzly Bear and She was Really Hungry.....
You Died........""")
    
    else:
        print(r"""
==========================================================================
You stumble into the dark room and notice something shining in the corner,
You found the treasuere!!!!!!!
==========================================================================
""")
    gameOver = True