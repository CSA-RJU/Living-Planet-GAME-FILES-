# Riley Underwood
# Practicum IT
# 11/3/19
##                 END OF TERMS AND CONDITIONS

##        How to Apply These Terms to Your New Programs
##If you develop a new program, and you want it to be of the greatest possible use to the public, the best way to achieve this is to make it free software which every_one can redistribute and change under these terms.

##To do so, attach the following notices to the program. It is safest to attach them to the start of each source file to most effectively state the exclusion of warranty; and each file should have at least the "copyright" line and a pointer to where the full notice is found.
##
##{one line to give the program's name and a brief idea of what it does.}
##Copyright (C) 2018  {name of author}

##This program is free software: you can redistribute it and/or modify
##it under the terms of the GNU General Public License as published by
##the Free Software Foundation, either version 3 of the License, or
##(at your option) any later version.

##This program is distributed in the hope that it will be useful,
##but WITHOUT ANY WARRANTY; without even the implied warranty of
##MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##GNU General Public License for more details.

##You should have received a copy of the GNU General Public License
##along with this program.  If not, see <http://www.gnu.org/licenses/>.
##Also add information on how to contact you by electronic and paper mail.

##If the program does terminal interaction, make it output a short notice like this when it starts in an interactive mode:

##Living-Planet  Copyright (C) 2018  CSA-RJU
##This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
##This is free software, and you are welcome to redistribute it
##under certain conditions; type `show c' for details.
##The hypothetical commands show w' and show c' should show the appropriate parts of the General Public License. Of course, your program's commands might be different; for a GUI interface, you would use an "about box".

##You should also get your employer (if you work as a programmer) or school, if any, to sign a "copyright disclaimer" for the program, if necessary. For more information on this, and how to apply and follow the GNU GPL, see http://www.gnu.org/licenses/.

##The GNU General Public License does not permit incorporating your program into proprietary programs. If your program is a subroutine library, you may consider it more useful to permit linking proprietary applications with the library. If this is what you want to do, use the GNU Lesser General Public License instead of this License. But first, please read http://www.gnu.org/philosophy/why-not-lgpl.html.

# [Python imports]
import pygame
from sys import exit
from vector2d import Vector2D

# region [Globals]
# Misc. globals:
global block_0, stage, carry_on, gameplay, game_map, map_size_x, map_size_y, player_temp_x, player_temp_y, title_screen, stage_surface, stage_start_adjust_x, player_start_adjust_x, stage_coords, player_coords
# Controls:
global player_x, player_y, player_horizontal_acceleration_speed, player_horizontal_acceleration
global movement_horizontal_direction, stage_movement_x, player_vertical_acceleration, movement_vertical_direction
global player_vertical_acceleration_speed, stage_movement_y, land_adjust
# Stage 1:
global block_1, block_2, block_3, block_4, block_5, block_6, block_7, block_8, block_w
# Stage 2:
global block_01, block_02, block_03, block_04, block_05, block_06, block_07, block_08
# endregion

# region [Initialization]
SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent()

pygame.mixer.pre_init(48100, 16, 20, 0)  # Frequency, size, channels, buffer size.

pygame.init()

# FPS
clock = pygame.time.Clock()
# endregion

# region [Screen stats]
SCREENWIDTH = 1280
SCREENHEIGHT = 720
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Living Planet")
# endregion

# region [Definitions]
# region Misc. definitions.
stage = "none"
stage_coords = [0, 0]
player_coords = [0, 0]
title_planet_frame = 10
player_frame = 1
face = "right"
music_mute = False
god = False
# endregion

# region Horizontal stage movement
player_horizontal_acceleration_speed = 0
player_horizontal_acceleration = 0
movement_horizontal_direction = "none"
stage_movement_x = 0
max_speed_x = 10
stage_backdrop_movement_1 = [0 - 1280, 0]
stage_backdrop_movement_2 = [0, 0]
stage_backdrop_movement_3 = [0 + 1280, 0]
wall_to_right = False
wall_to_left = False
stage_start_adjust_x = 0
player_start_adjust_x = stage_start_adjust_x * -1
left_border_hit = False
# endregion

# region Vertical stage movement
player_vertical_acceleration_speed = 0
player_vertical_acceleration = 0
movement_vertical_direction = "none"
stage_movement_y = 0
max_speed_y = 15
touching_ground = True
land_adjust = 0
# endregion

# region Transitions
global transition_start_black, transition_time, transition_speed, transition_start_type, transition_end_type
transition_start_black = False
transition_load_black = False
transition_end_black = False
transition_start_type = "fast"
transition_end_type = "fast"
opacity = 0
transition_speed = 1  # How quickly the transition goes. (shade/frame)
transition_timer = 0
transition_time = 0  # How many frames the transition lasts for.
transition_time = 0
first_digit = 0
loading_frame = 1

rotation_direction = 0.  # At 0, the object will not rotate
# endregion
# endregion

# region [Surfaces]
transition_screen = pygame.Surface(screen.get_size())
transition_screen.fill((0, 0, 0))
transition_screen.set_alpha(opacity)

stage_surface = pygame.Surface(screen.get_size())
stage_surface.fill((255, 255, 254))
stage_surface.set_colorkey((255, 255, 254))
# endregion

# region [Images]
# region [Title screen]
title_space = pygame.image.load('Title Space.png').convert_alpha()
title_space = pygame.transform.scale(title_space, (1280, 720))

title_planet = pygame.image.load('LP Outer View Dormant.png').convert_alpha()
title_planet = pygame.transform.scale(title_planet, (800, 800))
title_planet_pos = Vector2D(950, 250)
title_planet_rotation = -5.  # How Rotated the image starts.
title_planet_rotation_speed = 30.  # Degrees per second.

title_text = pygame.image.load('Title Text.png').convert_alpha()
title_text = pygame.transform.scale(title_text, (1280, 720))

title_text_highlight = pygame.image.load('Title Text Highlight.png').convert_alpha()
title_text_highlight = pygame.transform.scale(title_text_highlight, (1280, 720))
# endregion

## region [Player]
player = pygame.image.load('Player BiggieMC(R) Idle (1).png').convert_alpha()
player = pygame.transform.scale(player, (100, 100))
# endregion

## region [Levels]
stage_1_background = pygame.image.load('Stage 1 Background.png').convert_alpha()
stage_1_background = pygame.transform.scale(stage_1_background, (1280, 720))
stage_1_backdrop = pygame.image.load('Stage 1 Backdrop.png').convert_alpha()
stage_1_backdrop = pygame.transform.scale(stage_1_backdrop, (1280, 720))
stage_2_background = pygame.image.load('Stage 2 Background.png').convert_alpha()
stage_2_background = pygame.transform.scale(stage_2_background, (1280, 720))
# endregion

## region [Paused]
paused_text = pygame.image.load('Paused Text Alt.png').convert_alpha()
paused_text = pygame.transform.scale(paused_text, (1280, 720))
# endregion

# region [Loading screen]
loading_screen = pygame.image.load('Loading Screen.png').convert_alpha()
loading_screen = pygame.transform.scale(loading_screen, (1280, 720))

loading_frame_1 = pygame.image.load('Loading Frame (1).png').convert_alpha()
loading_frame_1 = pygame.transform.scale(loading_frame_1, (90, 90))
loading_frame_2 = pygame.image.load('Loading Frame (2).png').convert_alpha()
loading_frame_2 = pygame.transform.scale(loading_frame_2, (90, 90))
loading_frame_3 = pygame.image.load('Loading Frame (3).png').convert_alpha()
loading_frame_3 = pygame.transform.scale(loading_frame_3, (90, 90))
loading_frame_4 = pygame.image.load('Loading Frame (4).png').convert_alpha()
loading_frame_4 = pygame.transform.scale(loading_frame_4, (90, 90))
loading_frame_5 = pygame.image.load('Loading Frame (5).png').convert_alpha()
loading_frame_5 = pygame.transform.scale(loading_frame_5, (90, 90))
# endregion
# endregion

# region [Music]
title_song = pygame.mixer.music.load('Pure Numbness.wav')
# endregion


#################################################################################################### FUNCTIONS #############################################################################################


def Title_Screen():
    global every_on, carry_on, title_screen, stage, gameplay, paused
    every_on = True
    gameplay = False
    paused = False

    if music_mute is False:
        if title_screen is True:
            Titlesong = pygame.mixer.music.load('Pure Numbness.wav')
            pygame.mixer.music.play(-1)

    title_screen = True


def New_Game():
    global stage, gameplay
    stage = "Stage 1"
    gameplay = True

    # Stuff for doing a transition:
    global transition_start_black, transition_time, transition_speed, carry_on, transition_start_type, transition_end_type, title_screen
    carry_on = False
    opacity = 0
    loading_frame = 1
    transition_start_black = True
    transition_start_type = "fast"
    transition_end_type = "slow"
    transition_speed = 1  # How quickly the transition goes. (shade/frame)
    transition_time = 100  # How many frames the transition lasts for.

    title_screen = False


def Load_Game():
    global stage, gameplay
    stage = "Stage 2"
    gameplay = True

    # Stuff for doing a transition:
    global transition_start_black, transition_time, transition_speed, carry_on, transition_start_type, transition_end_type, title_screen
    carry_on = False
    opacity = 0
    loading_frame = 1
    transition_start_black = True
    transition_start_type = "fast"
    transition_end_type = "slow"
    transition_speed = 1  # How quickly the transition goes. (shade/frame)
    transition_time = 100  # How many frames the transition lasts for.

    title_screen = False


def Load_Map(stage):
    global game_map, map_size_x, map_size_y, player_temp_x, player_temp_y
    game_map = []
    map_load = open(f'{stage}.LPM', "r")
    line = map_load.readline()  # Reads the first line once to get it started.
    linesplit = line.split(",")
    map_size_x = int(linesplit[0])
    map_size_y = int(linesplit[1])
    player_temp_x = int(linesplit[2])
    player_temp_y = int(linesplit[3])
    line = map_load.readline()
    while line:  # Assures the program runs through the whole file.
        linesplit = line.split("'")
        column = []
        for f in linesplit:
            f = f.strip(" \n")
            column.append(f)
        game_map.append(column)
        line = map_load.readline()  # Assures that the program checks more than one line.
    map_load.close()


def Load_Stage():
    # Grabbing the player
    global map_size_x, map_size_y, player_x, player_y, stage_movement_x, stage_movement_y, stage_surface, stage_start_adjust_x, player_start_adjust_x, stage_coords

    player_x = int((player_temp_x - 1) * 50)
    player_y = int((player_temp_y - 1) * 50)
    stage_movement_x = 0
    stage_movement_y = 0
    stage_coords = [0, 0]

    if 0 >= (0 - float(player_x) + 590):
        stage_start_adjust_x = (0 - float(player_x) + 590) * -1
        player_start_adjust_x = stage_start_adjust_x * -1

    stage_surface = pygame.Surface(((map_size_x * 50), (map_size_y * 50)))
    stage_surface.fill((255, 255, 254))
    stage_surface.set_colorkey((255, 255, 254))

    # Grabbing the blocks
    global game_map, block_0, stage
    block_0 = pygame.image.load('Block 0.png').convert_alpha()
    block_0 = pygame.transform.scale(block_0, (50, 50))
    if stage == "Stage 1":  # Loads in the blocks in stage 1.
        global block_1, block_2, block_3, block_4, block_5, block_6, block_7, block_8, block_w
        block_2 = pygame.image.load('Block 2.png').convert_alpha()
        block_2 = pygame.transform.scale(block_2, (50, 50))
        block_3 = pygame.image.load('Block 3.png').convert_alpha()
        block_3 = pygame.transform.scale(block_3, (50, 50))
        block_4 = pygame.image.load('Block 4.png').convert_alpha()
        block_4 = pygame.transform.scale(block_4, (50, 50))
        block_5 = pygame.image.load('Block 5.png').convert_alpha()
        block_5 = pygame.transform.scale(block_5, (50, 50))
        block_6 = pygame.image.load('Block 6.png').convert_alpha()
        block_6 = pygame.transform.scale(block_6, (50, 50))
        block_7 = pygame.image.load('Block 7.png').convert_alpha()
        block_7 = pygame.transform.scale(block_7, (50, 50))
        block_8 = pygame.image.load('Block 8.png').convert_alpha()
        block_8 = pygame.transform.scale(block_8, (50, 50))
        block_w = pygame.image.load('Block w.png').convert_alpha()
        block_w = pygame.transform.scale(block_w, (50, 50))
    elif stage == "Stage 2":
        global block_01, block_02, block_03, block_04, block_05, block_06, block_07, block_08
        block_02 = pygame.image.load('Block 02.png').convert_alpha()
        block_02 = pygame.transform.scale(block_02, (50, 50))
        block_03 = pygame.image.load('Block 03.png').convert_alpha()
        block_03 = pygame.transform.scale(block_03, (50, 50))
        block_04 = pygame.image.load('Block 04.png').convert_alpha()
        block_04 = pygame.transform.scale(block_04, (50, 50))
        block_05 = pygame.image.load('Block 05.png').convert_alpha()
        block_05 = pygame.transform.scale(block_05, (50, 50))
        block_06 = pygame.image.load('Block 06.png').convert_alpha()
        block_06 = pygame.transform.scale(block_06, (50, 50))
        block_07 = pygame.image.load('Block 07.png').convert_alpha()
        block_07 = pygame.transform.scale(block_07, (50, 50))
        block_08 = pygame.image.load('Block 08.png').convert_alpha()
        block_08 = pygame.transform.scale(block_08, (50, 50))

    for y in range(map_size_y):  # Runs through the map list separating every line in the y axis.
        for x in range(map_size_x):  # Runs through the map list separating every item in the x axis in every separation line of the y axis.
            if stage == "Stage 1":  # Renders every block in the level and blits it to the stage surface.
                if game_map[y][x] == '[0]':  # v-- Detects what block goes in which place and blits them. --v
                    stage_surface.blit(block_0, ((((x * 50) - float(player_x) + 590) + stage_start_adjust_x),
                                       ((y * 50) - float(player_y)) + 310))
                elif game_map[y][x] == '[2]':
                    stage_surface.blit(block_2, ((((x * 50) - float(player_x) + 590) + stage_start_adjust_x),
                                       ((y * 50) - float(player_y)) + 310))
                elif game_map[y][x] == '[3]':
                    stage_surface.blit(block_3, ((((x * 50) - float(player_x) + 590) + stage_start_adjust_x),
                                       ((y * 50) - float(player_y)) + 310))
                elif game_map[y][x] == '[4]':
                    stage_surface.blit(block_4, ((((x * 50) - float(player_x) + 590) + stage_start_adjust_x),
                                       ((y * 50) - float(player_y)) + 310))
                elif game_map[y][x] == '[5]':
                    stage_surface.blit(block_5, ((((x * 50) - float(player_x) + 590) + stage_start_adjust_x),
                                       ((y * 50) - float(player_y)) + 310))
                elif game_map[y][x] == '[6]':
                    stage_surface.blit(block_6, ((((x * 50) - float(player_x) + 590) + stage_start_adjust_x),
                                       ((y * 50) - float(player_y)) + 310))
                elif game_map[y][x] == '[7]':
                    stage_surface.blit(block_7, ((((x * 50) - float(player_x) + 590) + stage_start_adjust_x),
                                       ((y * 50) - float(player_y)) + 310))
                elif game_map[y][x] == '[8]':
                    stage_surface.blit(block_8, ((((x * 50) - float(player_x) + 590) + stage_start_adjust_x),
                                       ((y * 50) - float(player_y)) + 310))
                elif game_map[y][x] == '[w]':
                    stage_surface.blit(block_w, ((((x * 50) - float(player_x) + 590) + stage_start_adjust_x),
                                       ((y * 50) - float(player_y)) + 310))

            elif stage == "Stage 2":
                if game_map[y][x] == '[0]':  # v-- Detects what block goes in which place and blits them. --v
                    stage_surface.blit(block_0, ((((x * 50) - float(player_x) + 590) + stage_start_adjust_x),
                                       ((y * 50) - float(player_y)) + 310))
                elif game_map[y][x] == '[2]':
                    stage_surface.blit(block_02, ((((x * 50) - float(player_x) + 590) + stage_start_adjust_x),
                                       ((y * 50) - float(player_y)) + 310))
                elif game_map[y][x] == '[3]':
                    stage_surface.blit(block_03, ((((x * 50) - float(player_x) + 590) + stage_start_adjust_x),
                                       ((y * 50) - float(player_y)) + 310))
                elif game_map[y][x] == '[4]':
                    stage_surface.blit(block_04, ((((x * 50) - float(player_x) + 590) + stage_start_adjust_x),
                                       ((y * 50) - float(player_y)) + 310))
                elif game_map[y][x] == '[5]':
                    stage_surface.blit(block_05, ((((x * 50) - float(player_x) + 590) + stage_start_adjust_x),
                                       ((y * 50) - float(player_y)) + 310))
                elif game_map[y][x] == '[6]':
                    stage_surface.blit(block_06, ((((x * 50) - float(player_x) + 590) + stage_start_adjust_x),
                                       ((y * 50) - float(player_y)) + 310))
                elif game_map[y][x] == '[7]':
                    stage_surface.blit(block_07, ((((x * 50) - float(player_x) + 590) + stage_start_adjust_x),
                                       ((y * 50) - float(player_y)) + 310))
                elif game_map[y][x] == '[8]':
                    stage_surface.blit(block_08, ((((x * 50) - float(player_x) + 590) + stage_start_adjust_x),
                                       ((y * 50) - float(player_y)) + 310))


def Pause():  # Pauses the game.
    global carry_on, paused
    paused = True


def Unpause():  # Unpauses the game.
    global carry_on, paused
    paused = False


######################################################################################## RUNNING THE GAME #############################################################################################

every_on = True
carry_on = True
title_screen = True
gameplay = False
paused = False
pygame.mixer.music.stop()
Title_Screen()

while every_on:  # Anything that updates ever.
    # print(clock)  # Prints the frame rate.

    mousexy = pygame.mouse.get_pos()
    # print(mousexy)

############################################################################################ One-tap key input ########################################################################

    # To pause/quit the game
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()

            # When "P" is pressed
            if event.key == pygame.K_p:
                if paused is False:
                    Pause()
                elif paused is True:
                    Unpause()

        # region [Buttons]

        # Moving the mouse:
        if event.type == pygame.MOUSEMOTION:
            pass
        if event.type == pygame.MOUSEBUTTONDOWN:
            if carry_on:
                # Title screen buttons:
                if title_screen is True and transition_end_black is False:  # Only on title screen and after a transition has finished can this happen.
                    # New Game button
                    if 408 <= mousexy[0] <= 875 and 304 <= mousexy[1] <= 384:
                        New_Game()
                    # Load Game button
                    if 408 <= mousexy[0] <= 875 and 408 <= mousexy[1] <= 488:
                        Load_Game()
                    # Options button
                    if 408 <= mousexy[0] <= 875 and 508 <= mousexy[1] <= 588:
                        print("Extras coming soon!")
                    # Leave button
                    if 408 <= mousexy[0] <= 875 and 612 <= mousexy[1] <= 692:
                        carry_on = False
                        every_on = False
                    # Extras button
                    if 408 <= mousexy[0] <= 875 and 719 <= mousexy[1] <= 799:
                        print("Extras coming soon!")

                # Pause buttons:
                if paused is True and transition_end_black is False:  # Only on title screen and after a transition has finished can this happen.
                    # Main Menu button
                    if 408 <= mousexy[0] <= 875 and 304 <= mousexy[1] <= 384:
                        # Stuff for doing a transition:
                        carry_on = False
                        opacity = 0
                        loading_frame = 1
                        transition_start_black = True
                        transition_start_type = "fast"
                        transition_end_type = "fast"
                        transition_speed = 1  # How quickly the transition goes. (shade/frame)
                        transition_time = 100  # How many frames the transition lasts for.
                        Title_Screen()
                    # Options button
                    if 408 <= mousexy[0] <= 875 and 508 <= mousexy[1] <= 588:
                        print("Extras coming soon!")
                    # Leave button
                    if 408 <= mousexy[0] <= 875 and 612 <= mousexy[1] <= 692:
                        carry_on = False
                        every_on = False
        # endregion

    if carry_on:  # When not paused.

        # region [Title screen]

        if title_screen is True:

            # region [Planet stuff]
            rotated_title_planet = pygame.transform.rotate(title_planet, title_planet_rotation)  # Return the rotated_title_planet surface object
            ##          w, h = rotated_title_planet.get_size()
            title_planet_draw_pos = Vector2D(title_planet_pos.x - 800 / 2, title_planet_pos.y - 800 / 2)

            time_passed = clock.tick()
            time_passed_seconds = time_passed / 1000.0

            title_planet_rotation += rotation_direction * title_planet_rotation_speed * time_passed_seconds

            # Blitting images.
            screen.blit(title_space, (0, 0))
            screen.blit(rotated_title_planet, title_planet_draw_pos)
            screen.blit(title_text, (0, 0))

            # Rotating planet on title screen.
            if title_planet_frame >= 1:
                title_planet_frame -= 1
            else:
                title_planet_frame = 160
                if rotation_direction == 0 or rotation_direction == .01:
                    rotation_direction = -.01
                else:
                    rotation_direction = .01
            # endregion

            # region [Button highlights]
            if transition_end_black is False:  # Only after a transition has finished can this happen.
                # New Game button
                if 408 <= mousexy[0] <= 875 and 305 <= mousexy[1] <= 385:
                    screen.blit(title_text_highlight, (0, 0))
                # Load Game button
                if 408 <= mousexy[0] <= 875 and 408 <= mousexy[1] <= 488:
                    screen.blit(title_text_highlight, (0, 104))
                # Options button
                if 408 <= mousexy[0] <= 875 and 508 <= mousexy[1] <= 588:
                    screen.blit(title_text_highlight, (0, 204))
                # Leave button
                if 408 <= mousexy[0] <= 875 and 612 <= mousexy[1] <= 692:
                    screen.blit(title_text_highlight, (0, 308))
                # Extras button
                if 408 <= mousexy[0] <= 875 and 719 <= mousexy[1] <= 799:
                    screen.blit(title_text_highlight, (0, 415))
            # endregion

        else:
            if gameplay is False:
                screen.blit(title_space, (0, 0))
        # endregion

        # region [Controls]

        if title_screen is False and paused is False and transition_end_black is False:  # When Playing the game.

            # region [Left]
            if key[pygame.K_a]:
                if not wall_to_left:
                    face = "left"
                    if movement_horizontal_direction != "left":
                        movement_horizontal_direction = "left"
                        player_horizontal_acceleration = 0
                        player_horizontal_acceleration_speed = 0
                    if player_horizontal_acceleration > -max_speed_x and movement_horizontal_direction == "left":  # Left.
                        player_horizontal_acceleration_speed += -.08
                        player_horizontal_acceleration += (-.16 + player_horizontal_acceleration_speed)
                        if player_horizontal_acceleration < -max_speed_x:  # Max speed.
                            player_horizontal_acceleration = -max_speed_x
                            player_horizontal_acceleration_speed = 0
                elif player_horizontal_acceleration < 0 and movement_horizontal_direction != "right":  # Idle after moving left.
                    player_horizontal_acceleration_speed += .08
                    player_horizontal_acceleration += (.16 + player_horizontal_acceleration_speed)
                    if player_horizontal_acceleration > 0:  # When idle, the acceleration will round to 0 if it is close enough.
                        player_horizontal_acceleration = 0
                        player_horizontal_acceleration_speed = 0

                if wall_to_left:
                    player_horizontal_acceleration = 0
                    player_horizontal_acceleration_speed = 0
            # endregion

            # region [Right]
            if key[pygame.K_d]:
                if not wall_to_right:
                    face = "right"
                    if movement_horizontal_direction != "right":
                        movement_horizontal_direction = "right"
                        player_horizontal_acceleration = 0
                        player_horizontal_acceleration_speed = 0
                    if player_horizontal_acceleration < max_speed_x and movement_horizontal_direction == "right":  # Right.
                        player_horizontal_acceleration_speed += .08
                        player_horizontal_acceleration += (.16 + player_horizontal_acceleration_speed)
                        if player_horizontal_acceleration > max_speed_x:  # Max speed.
                            player_horizontal_acceleration = max_speed_x
                            player_horizontal_acceleration_speed = 0
                elif player_horizontal_acceleration > 0 and movement_horizontal_direction != "left":  # Idle after moving right.
                    player_horizontal_acceleration_speed += -.08
                    player_horizontal_acceleration += (-.16 + player_horizontal_acceleration_speed)
                    if player_horizontal_acceleration < 0:  # When idle, the acceleration will round to 0 if it is close enough.
                        player_horizontal_acceleration = 0
                        player_horizontal_acceleration_speed = 0

                if wall_to_right:
                    player_horizontal_acceleration = 0
                    player_horizontal_acceleration_speed = 0
            # endregion

            if not key[pygame.K_a] and not key[pygame.K_d]:  # Not pressing "a" or "d".
                movement_horizontal_direction = "none"

            if not god:
                # region [Up (Jumping)]
                if key[pygame.K_w]:
                    if touching_ground is True:
                        if player_vertical_acceleration == 0:
                            player_vertical_acceleration = max_speed_y  # This # controls the speed of the jump. (Starting higher and decreasing)
                        touching_ground = False

                if not touching_ground:
                    if key[pygame.K_w]:
                        if player_vertical_acceleration > 0:
                            player_vertical_acceleration -= .5  # This # controls how high the player jumps. (The lower the number the higher the jump)
                        elif player_vertical_acceleration > -max_speed_y:  # This # controls the speed of the jump. (Starting higher and decreasing)
                            player_vertical_acceleration -= 1
                        elif player_vertical_acceleration > 0:
                            player_vertical_acceleration = 0
                    else:
                        if player_vertical_acceleration > 0:
                            player_vertical_acceleration -= 1  # This # controls how high the player jumps. (The lower the number the higher the jump)
                        elif player_vertical_acceleration > -max_speed_y:  # This # controls the speed of the jump. (Starting higher and decreasing)
                            player_vertical_acceleration -= 1
                        elif player_vertical_acceleration > 0:
                            player_vertical_acceleration = 0

                if touching_ground:
                    player_vertical_acceleration = 0
                # endregion

            if god:
                # region [Down]
                if key[pygame.K_s]:
                    if movement_vertical_direction != "down":
                        movement_vertical_direction = "down"
                        player_vertical_acceleration = 0
                        player_vertical_acceleration_speed = 0
                    if player_vertical_acceleration > -max_speed_x and movement_vertical_direction == "down":  # Left.
                        player_vertical_acceleration_speed += -.8
                        player_vertical_acceleration += (-.16 + player_vertical_acceleration_speed)
                        if player_vertical_acceleration < -max_speed_x:
                            player_vertical_acceleration = -max_speed_x
                            player_vertical_acceleration_speed = 0
                elif player_vertical_acceleration < 0 and movement_vertical_direction != "up":  # Idle after moving left.
                    player_vertical_acceleration_speed += .08
                    player_vertical_acceleration += (.16 + player_vertical_acceleration_speed)
                    if player_vertical_acceleration > 0:  # When idle, the acceleration will round to 0 if it is close enough.
                        player_vertical_acceleration = 0
                        player_vertical_acceleration_speed = 0
                elif not key[pygame.K_w] and not key[pygame.K_s]:  # Not pressing "w" or "s".
                    movement_vertical_direction = "none"
                # endregion

                # region [Up]
                if key[pygame.K_w]:
                    if movement_vertical_direction != "up":
                        movement_vertical_direction = "up"
                        player_vertical_acceleration = 0
                        player_vertical_acceleration_speed = 0
                    if player_vertical_acceleration < max_speed_x and movement_vertical_direction == "up":  # Right.
                        player_vertical_acceleration_speed += .08
                        player_vertical_acceleration += (.16 + player_vertical_acceleration_speed)
                        if player_vertical_acceleration > max_speed_x:
                            player_vertical_acceleration = max_speed_x
                            player_vertical_acceleration_speed = 0
                elif player_vertical_acceleration > 0 and movement_vertical_direction != "down":  # Idle after moving right.
                    player_vertical_acceleration_speed += -.08
                    player_vertical_acceleration += (-.16 + player_vertical_acceleration_speed)
                    if player_vertical_acceleration < 0:  # When idle, the acceleration will round to 0 if it is close enough.
                        player_vertical_acceleration = 0
                        player_vertical_acceleration_speed = 0

                elif not key[pygame.K_w] and not key[pygame.K_s]:  # Not pressing "w" or "s".
                    movement_vertical_direction = "none"
                # endregion
        # endregion

############################################################################################## Stages ########################################################################

        if gameplay is True:
            if stage_coords[0] <= 0 and movement_horizontal_direction == "left":
                stage_movement_x += int(player_horizontal_acceleration)
            elif movement_horizontal_direction == "right":
                stage_movement_x += int(player_horizontal_acceleration)
            stage_movement_y += int(player_vertical_acceleration)

            touching_ground = None  # Resets the block sensor (if the player is touching the block).if stage_movement_x != (round(stage_movement_x / 50) * 50) - 21 and stage_movement_y == (round(stage_movement_y / 50) * 50):
            wall_to_right = None  # Resets the block sensor (if the player is touching the block).
            wall_to_left = None  # Resets the block sensor (if the player is touching the block).

            for y in range(map_size_y):  # Runs through the map list separating every line in the y axis.
                for x in range(map_size_x):  # Runs through the map list separating every item in the x axis in every separation line of the y axis.
                    if stage == "Stage 1" or stage == "Stage 2":
                        if game_map[y][x] == '[2]' or game_map[y][x] == '[3]' or game_map[y][x] == '[4]':  # Defines the hit box.
        #  The player's border --v          v-- The selected block's current position --v
                            if (360 <= (((y * 50) - float(player_y)) + 310) + stage_movement_y <= 410) and (
                                    570 <= (((x * 50) - float(player_x)) + 590) - stage_movement_x <= 660):
                                touching_ground = True
                                stage_movement_y = (round(stage_movement_y / 50) * 50)
                                if game_map[y][x] == '[3]' or game_map[y][x] == '[4]':  # Defines the hit box.
                                    if (((y * 50) - float(player_y)) + 310) + stage_movement_y <= 409:
                                        if game_map[y][x] == '[3]':
                                            stage_movement_x = (round(stage_movement_x / 50) * 50) - 21
                                            wall_to_right = True
                                        if game_map[y][x] == '[4]':
                                            stage_movement_x = (round(stage_movement_x / 50) * 50) + 21
                                            wall_to_left = True
                        if (360 <= (((y * 50) - float(player_y)) + 310) + stage_movement_y <= 410) and (
                                570 <= (((x * 50) - float(player_x)) + 590) - stage_movement_x <= 660):
                            if game_map[y][x] == '[7]':  # Defines the hit box.
                                wall_to_right = True
                            elif game_map[y][x] == '[8]':  # Defines the hit box.
                                wall_to_left = True

            if touching_ground is True:
                player_vertical_acceleration = 0

            # region [Backdrop movement]
            if left_border_hit is False:
                stage_backdrop_movement_1[0] = (0 - 1280 - (stage_movement_x / 16))
            stage_backdrop_movement_1[1] = (0 + (stage_movement_y / 32))
            if left_border_hit is False:
                stage_backdrop_movement_2[0] = (0 - (stage_movement_x / 16))
            stage_backdrop_movement_2[1] = (0 + (stage_movement_y / 32))
            if left_border_hit is False:
                stage_backdrop_movement_3[0] = (0 - 1280 + (stage_movement_x / 16))
            stage_backdrop_movement_3[1] = (0 + (stage_movement_y / 32))

            # Loops the backdrop so that it feels infinite:
            if stage_backdrop_movement_1[0] < -1280:
                stage_backdrop_movement_1[0] += 2560
            elif stage_backdrop_movement_1[0] > 1280:
                stage_backdrop_movement_1[0] -= 2560
            if stage_backdrop_movement_2[0] < -1280:
                stage_backdrop_movement_2[0] += 2560
            elif stage_backdrop_movement_2[0] > 1280:
                stage_backdrop_movement_2[0] -= 2560
            if stage_backdrop_movement_3[0] < -1280:
                stage_backdrop_movement_3[0] += 2560
            elif stage_backdrop_movement_3[0] > 1280:
                stage_backdrop_movement_3[0] -= 2560
            # endregion

            if stage == "Stage 1":
                screen.blit(stage_1_background, (0, 0))
                screen.blit(stage_1_backdrop, (stage_backdrop_movement_1[0], stage_backdrop_movement_1[1]))
                screen.blit(stage_1_backdrop, (stage_backdrop_movement_2[0], stage_backdrop_movement_1[1]))
                screen.blit(stage_1_backdrop, (stage_backdrop_movement_1[0], stage_backdrop_movement_1[1]))
            if stage == "Stage 2":
                screen.blit(stage_2_background, (0, 0))

            # Stage movement
            stage_coords[0] = (0 - stage_movement_x) - stage_start_adjust_x
            if stage_coords[0] >= 0:  # Adjusts the screen to not move past the left border.
                left_border_hit = True
                stage_coords[0] = 0
                player_coords[0] = (590 + stage_movement_x) + stage_start_adjust_x  # Makes the player on screen move instead of the stage.
            else:
                left_border_hit = False
            stage_coords[1] = (0 + stage_movement_y)
            screen.blit(stage_surface, (stage_coords[0], stage_coords[1]))

            # Player animation
            
            ## Setting a frame rate for the loading animation.
            if player_frame >= 12:  # (a) Must be divisible by itself and 10 more than b.
                player_frame -= 2  # (b) Speed of animation (frame of game/frame of animation) (Bigger # = faster)
            else:
                player_frame = 58  # (c) Must be divisible by itself, first digit must be the number of frames and last digit must be b less than a multiple of 10.

            ## Shows the first digit of the variable responsible for counting frames
            stopper = 0
            for i in str(player_frame):
                stopper += 1  # Stops in what ever place the # indicates.
                if stopper == 1:
                    first_digit = int(i)

            # Blitting the different frames of the loading animation.
            if face == "right":
                if first_digit == 1:
                    player = pygame.image.load('Player BiggieMC(R) Idle (5).png').convert_alpha()
                elif first_digit == 2:
                    player = pygame.image.load('Player BiggieMC(R) Idle (4).png').convert_alpha()
                elif first_digit == 3:
                    player = pygame.image.load('Player BiggieMC(R) Idle (3).png').convert_alpha()
                elif first_digit == 4:
                    player = pygame.image.load('Player BiggieMC(R) Idle (2).png').convert_alpha()
                elif first_digit == 5:
                    player = pygame.image.load('Player BiggieMC(R) Idle (1).png').convert_alpha()
            if face == "left":
                if first_digit == 1:
                    player = pygame.image.load('Player BiggieMC(L).png').convert_alpha()

            # Jumping animation.
            if not touching_ground:
                if player_vertical_acceleration > 3:  # 
                     player = pygame.image.load('Player BiggieMC(R) Jump (1).png').convert_alpha()
                if player_vertical_acceleration <= 3 and player_vertical_acceleration >= -3:
                     player = pygame.image.load('Player BiggieMC(R) Jump (2).png').convert_alpha()
                if player_vertical_acceleration < -3:
                     player = pygame.image.load('Player BiggieMC(R) Jump (3).png').convert_alpha()

            player = pygame.transform.scale(player, (100, 100))
            
            if left_border_hit is True:
                screen.blit(player, (player_coords[0], 310))  # (x, y) Moves the player to adjust for stage not moving.
            else:
                screen.blit(player, (590, 310))  # (x, y) Prints the player at the center of the screen

################################################################################################ Paused ##################################################################################

            if title_screen is False and paused is True:
                screen.blit(paused_text, (0, 0))

                if transition_end_black is False:  # Only after a transition has finished can this happen.
                    # New game button
                    if 408 <= mousexy[0] <= 875 and 305 <= mousexy[1] <= 385:
                        screen.blit(title_text_highlight, (0, 0))
                    # Load game button
                    if 408 <= mousexy[0] <= 875 and 408 <= mousexy[1] <= 488:
                        screen.blit(title_text_highlight, (0, 104))
                    # Ex-content button
                    if 408 <= mousexy[0] <= 875 and 508 <= mousexy[1] <= 588: 
                        screen.blit(title_text_highlight, (0, 204))
                    # Leave button
                    if 408 <= mousexy[0] <= 875 and 612 <= mousexy[1] <= 692:
                        screen.blit(title_text_highlight, (0, 308))
                    # Extras button
                    if 408 <= mousexy[0] <= 875 and 719 <= mousexy[1] <= 799:
                        screen.blit(title_text_highlight, (0, 415))

###################################################################################### Transitions ##################################################################################

    # Fading in:
    if transition_start_type == "fast" or transition_start_type == "slow":
        if transition_start_black is True and transition_end_black is False:
            if opacity < 255:  # max opacity.
                opacity += (transition_speed * 2)  # How quickly the transition goes. (shade/frame)
                transition_screen = pygame.Surface(screen.get_size())
                transition_screen.fill((0, 0, 0))
                if carry_on:
                    transition_screen.set_alpha(opacity)
                else:
                    transition_screen.set_alpha(opacity / (transition_speed * 10))
                screen.blit(transition_screen, (0, 0))
            else:  # Passing on the transition phase.
                transition_start_black = False
                transition_load_black = True
                transition_timer = 0
                Load_Map(stage)
                Load_Stage()
                pygame.mixer.music.stop()

    # Loading screen:
    if transition_timer < transition_time and transition_load_black is True:
        transition_timer += 1
        opacity = 255
        transition_screen.set_alpha(opacity)
        screen.blit(transition_screen, (0, 0))
        screen.blit(loading_screen, (0, 0))

        # Loading Animation
        ## Setting a frame rate for the loading animation.
        if loading_frame >= 12:  # (a) Must be divisible by itself and 10 more than b.
            loading_frame -= 1  # (b) Speed of animation (frame of game/frame of animation) (Bigger # = faster)
        else:
            loading_frame = 59  # (c) Must be divisible by itself, first digit must be the number of frames and last digit must be b less than a multiple of 10.

        ## Shows the first digit of the variable responsible for counting frames
        stopper = 0
        for i in str(loading_frame):
            stopper += 1  # Stops in what ever place the # indicates.
            if stopper == 1:
                first_digit = int(i)

        # Blitting the different frames of the loading animation.
        if first_digit == 1:
            screen.blit(loading_frame_5, (595, 500))
        elif first_digit == 2:
            screen.blit(loading_frame_4, (595, 500))
        elif first_digit == 3:
            screen.blit(loading_frame_3, (595, 500))
        elif first_digit == 4:
            screen.blit(loading_frame_2, (595, 500))
        elif first_digit == 5:
            screen.blit(loading_frame_1, (595, 500))

    else:  # Passing on the transition phase.
        if transition_load_black is True:
            transition_timer = 0
            transition_load_black = False
            transition_end_black = True
            carry_on = True
            if music_mute is False:  # Playing music
                if title_screen is True:
                    Titlesong = pygame.mixer.music.load('Pure Numbness.wav')
                    pygame.mixer.music.play(-1)
                else:
                    if stage == "Stage 1":  # v-- Plays music when loading stops. --v
                        Stage_1 = pygame.mixer.music.load('Home World Theme.wav')
                        pygame.mixer.music.play(-1)
                    elif stage == "Stage 2":
                        Stage_1 = pygame.mixer.music.load('Success.wav')
                        pygame.mixer.music.play(-1)

    # Fading out:
    if transition_end_black is True and transition_start_black is False:
        if opacity > 0:
            if transition_end_type == "fast":
                opacity -= (transition_speed * 5)  # How quickly the transition goes. (shade/frame)
            elif transition_end_type == "slow":
                opacity -= (transition_speed * 2)  # How quickly the transition goes. (shade/frame)
            transition_screen = pygame.Surface(screen.get_size())
            transition_screen.fill((0, 0, 0))
            if carry_on:
                transition_screen.set_alpha(opacity)
            else:
                transition_screen.set_alpha(opacity)
            screen.blit(transition_screen, (0, 0))
        else:  # Ending the transition phase.
            transition_end_black = False

###################################################################################### Extras at End ##################################################################################

    # Refresh Screen
    pygame.display.flip()

    # FPS
    clock.tick(60)

pygame.quit()
exit()
