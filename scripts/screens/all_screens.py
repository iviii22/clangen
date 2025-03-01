from .AllegiancesScreen import AllegiancesScreen
from .CeremonyScreen import CeremonyScreen
from .ChangeGenderScreen import ChangeGenderScreen
from .ChooseAdoptiveParentScreen import ChooseAdoptiveParentScreen
from .ChooseMateScreen import ChooseMateScreen
from .ChooseMentorScreen import ChooseMentorScreen
from .ClanScreen import ClanScreen
from .ClanSettingsScreen import ClanSettingsScreen
from .ClearingScreen import ClearingScreen
from .EventsScreen import EventsScreen
from .FamilyTreeScreen import FamilyTreeScreen
from .LeaderDenScreen import LeaderDenScreen
from .ListScreen import ListScreen
from .MakeClanScreen import MakeClanScreen
from .MedDenScreen import MedDenScreen
from .MediationScreen import MediationScreen
from .PatrolScreen import PatrolScreen
from .ProfileScreen import ProfileScreen
from .RelationshipScreen import RelationshipScreen
from .RoleScreen import RoleScreen
from .Screens import Screens
from .SettingsScreen import SettingsScreen
from .SpriteInspectScreen import SpriteInspectScreen
from .StartScreen import StartScreen
from .SwitchClanScreen import SwitchClanScreen
from .WarriorDenScreen import WarriorDenScreen
from .NurseryScreen import NurseryScreen

# ---------------------------------------------------------------------------- #
#                                  UI RULES                                    #
# ---------------------------------------------------------------------------- #
"""
SCREEN: 700 height x 800 width

MARGINS: 25px on all sides
    ~Any new buttons or text MUST be within these margins.
    ~Buttons on the edge of the screen should butt up right against the margin. 
    (i.e. the <<Main Menu button is placed 25px x 25px on most screens) 
    
BUTTONS:
    ~Buttons are 30px in height. Width can be anything, though generally try to keep to even numbers.
    ~Square icons are 34px x 34px.
    ~Generally keep text at least 5px away from the right and left /straight/ (do not count the rounded ends) edge 
    of the button (this rule is sometimes broken. the goal is to be consistent across the entire screen or button type)
    ~Generally, the vertical gap between buttons should be 5px
"""

# SCREENS
screens = Screens()

# ---------------------------------------------------------------------------- #
#                                 cat_screens.py                               #
# ---------------------------------------------------------------------------- #

profile_screen = ProfileScreen('profile screen')
ceremony_screen = CeremonyScreen('ceremony screen')
role_screen = RoleScreen('role screen')
sprite_inspect_screen = SpriteInspectScreen("sprite inspect screen")


make_clan_screen = MakeClanScreen('make clan screen')


allegiances_screen = AllegiancesScreen('allegiances screen')
camp_screen = ClanScreen('camp screen')
catlist_screen = ListScreen('list screen')
med_den_screen = MedDenScreen('med den screen')
freshkill_pile_screen = ClearingScreen('clearing screen')
warrior_den_screen = WarriorDenScreen('warrior den screen')
leader_den_screen = LeaderDenScreen('leader den screen')
nursery_screen = NurseryScreen('nursery screen')


events_screen = EventsScreen('events screen')


settings_screen = SettingsScreen('settings screen')
clan_settings_screen = ClanSettingsScreen('clan settings screen')
start_screen = StartScreen('start screen')
switch_clan_screen = SwitchClanScreen('switch clan screen')


patrol_screen = PatrolScreen('patrol screen')


choose_mate_screen = ChooseMateScreen('choose mate screen')
choose_mentor_screen = ChooseMentorScreen('choose mentor screen')
choose_adoptive_parent_screen = ChooseAdoptiveParentScreen('choose adoptive parent screen')
relationship_screen = RelationshipScreen('relationship screen')
view_children_screen = FamilyTreeScreen('see kits screen')
mediation_screen = MediationScreen("mediation screen")
change_gender_screen = ChangeGenderScreen("change gender screen")

