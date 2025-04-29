#Exercise B
import pygame
get_name=False
name="nothing"
suitable_prefixes=["tutorial_file_forest_","tutorial_file_desert_"]
count=0
while get_name==False:
    name=input("What is the name of the file?")
    prefix=input("And its prefix? [tutorial_file_desert_ or tutorial_file_forest_]")
    if prefix not in suitable_prefixes:
        print("Please input a suitable prefix")
    else:
        try:
            files1=open(name,"r")
            try:
                for temp in files1:
                    count+=1
                files1.close()
                files2=open(name,"r")
                pseudo_state=(files2.readlines()[1])
                pseudo_nums=pseudo_state.split(",")
                files2.close()
                map_screen=pygame.display.set_mode([(len(pseudo_nums)-1)*64,(count-1)*64])
                nums=[]
                for pseudo_count in range(count-1):
                    files3=open(name,"r")
                    state=(files3.readlines()[pseudo_count+1])
                    nums=state.split(",")
                    for j in range(len(nums)-1):
                        try:
                            numbers=nums[j]
                            try:
                                picture=pygame.image.load(prefix+numbers+".gif")
                                map_screen.blit(picture,(j*64,(pseudo_count)*64))
                                #pygame.display.update()
                                #pygame.time.delay(5000)
                                get_name=True
                            except:
                                print("Numbers are between 0 and 4; there was not a suitable image to place it.")
                            pygame.display.update()
                            pygame.time.delay(50)



                        except:
                            print("The file does not have integers.")
                    files3.close()

            except:
                print("It doesn't have lines to read.")
        except:
            print("It doesn't work properly.")
