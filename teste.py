from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

BOAT = """
                 __/___            
           _____/______|           
   _______/_____\_______\_____     
   \              < < <       |"""

SEA = Back.BLUE + """~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""" + Style.RESET_ALL

EXPLOSION ="""
           _ ._  _ , _ ._        
        (_ ' ( `  )_  .__)       
      ( (  (    )   `)  ) _)     
     (__ (_   (_ . _) _) ,__)    
         `~~`\ ' . /`~~`         
              ;   ;              
              /  \\               
_____________/_ __ \_____________"""

TITLE = """
······················································
: ██████╗  █████╗ ████████╗████████╗██╗     ███████╗ :
: ██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝ :
: ██████╔╝███████║   ██║      ██║   ██║     █████╗   :
: ██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝   :
: ██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗ :
: ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝ :
:                                                    :
: ███████╗██╗███████╗██╗     ██████╗                 :
: ██╔════╝██║██╔════╝██║     ██╔══██╗                :
: █████╗  ██║█████╗  ██║     ██║  ██║                :
: ██╔══╝  ██║██╔══╝  ██║     ██║  ██║                :
: ██║     ██║███████╗███████╗██████╔╝                :
: ╚═╝     ╚═╝╚══════╝╚══════╝╚═════╝                 :
······················································
"""

print(BOAT)
print(Back.BLUE + SEA + Style.RESET_ALL)

print(Back.WHITE + Fore.RED + EXPLOSION + Style.RESET_ALL)
print(Back.BLUE + SEA + Style.RESET_ALL)

print(Fore.LIGHTBLUE_EX + TITLE + Style.RESET_ALL)
print(SEA)