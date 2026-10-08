import os
import random
import re
import sys
import textwrap
import time

# --- TERMINAL STYLING & ANSI COLORS ---
class Color:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"


BOX_WIDTH = 68  # Standardized inner width across all UI cards


def render_box_line(text="", color_code=Color.CYAN):
    """Renders a single line inside border walls with exact padding."""
    visible_text = text
    for color in [Color.RESET, Color.BOLD, Color.DIM, Color.ITALIC, 
                  Color.RED, Color.GREEN, Color.YELLOW, Color.BLUE, 
                  Color.MAGENTA, Color.CYAN, Color.WHITE, Color.BG_RED, Color.BG_GREEN]:
        visible_text = visible_text.replace(color, "")

    padding = BOX_WIDTH - len(visible_text)
    if padding < 0:
        padding = 0
    return f"{color_code}│{Color.RESET} {text}{' ' * padding} {color_code}│{Color.RESET}"


class Sound:
    @staticmethod
    def play_beep(count=1, delay=0.1):
        for _ in range(count):
            sys.stdout.write("\007")
            sys.stdout.flush()
            time.sleep(delay)

    @staticmethod
    def clue_reveal():
        Sound.play_beep(1)

    @staticmethod
    def case_solved():
        Sound.play_beep(3, 0.15)

    @staticmethod
    def case_failed():
        Sound.play_beep(2, 0.3)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def type_writer(text, speed=0.012):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()


# --- PLAYER STATS ---
class DetectiveStats:
    def __init__(self):
        self.cases_solved = 0
        self.cases_failed = 0
        self.win_streak = 0
        self.score = 0

    @property
    def total_cases(self):
        return self.cases_solved + self.cases_failed

    @property
    def accuracy(self):
        if self.total_cases == 0:
            return 0.0
        return (self.cases_solved / self.total_cases) * 100

    @property
    def rank(self):
        if self.score >= 1000:
            return "Master Detective"
        elif self.score >= 500:
            return "Senior Investigator"
        elif self.score >= 200:
            return "Private Eye"
        else:
            return "Rookie Cop"


# --- SUSPECT & MYSTERY DATA ---
class Suspect:
    def __init__(self, name, role, look, style, quirk, true_alibis, fake_alibis, true_motives, fake_motives, clues):
        self.name = name
        self.role = role
        self.look = look
        self.style = style
        self.quirk = quirk
        self.true_alibis = true_alibis
        self.fake_alibis = fake_alibis
        self.true_motives = true_motives
        self.fake_motives = fake_motives
        self.clues = clues
        self.current_vibe = ""
        self.is_lying = False

    def randomize_round_state(self, force_lie=False, lie_chance=0.35):
        """Randomizes the suspect's demeanor and determines if they will lie in this round."""
        vibes = ["Nervous & fidgety", "Overly confident", "Cold & defensive", "Sarcastic & aloof", "Quietly intense"]
        self.current_vibe = random.choice(vibes)
        
        # Suspect lies if forced (e.g. culprit on Hard) or randomly based on lie_chance
        if force_lie:
            self.is_lying = True
        else:
            self.is_lying = random.random() < lie_chance


class Mystery:
    def __init__(self, difficulty, stats):
        self.difficulty = difficulty
        self.stats = stats
        self.interrogation_count = 0
        self.visited_locations = set()

        self.locations = [
            "Mess Hall & Campfire",
            "The Tent Grid",
            "Outer Woods & Ridge",
            "Boathouse & Docks"
        ]

        self.suspects = [
            Suspect(
                name="Greg",
                role="Sidequest Host",
                look="Tall teenage guy with green eyes, short brown hair, and black-rimmed glasses.",
                style="Vintage denim vest, cargo pants, and a signature embroidered snapback cap.",
                quirk="Constantly pushes his glasses up his nose and taps his key ring.",
                true_alibis=[
                    "I was maintaining the campfire near the mess hall until 10 PM.",
                    "I was organizing the scavenger hunt props near the main cabin.",
                    "I was helping set up nighttime lantern posts along the trail."
                ],
                fake_alibis=[
                    "I was alone in my cabin reading all night—nobody saw me.",
                    "I was fixing a broken kayak down at the docks around that time.",
                    "I was asleep early in my bunk after a long day of hosting."
                ],
                true_motives=[
                    "Feared the victim was going to report him for mismanaging sidequests.",
                    "Had an argument with the victim over a stolen collector's cap.",
                    "Felt insulted when the victim mocked his sidequest setup."
                ],
                fake_motives=[
                    "Claims he had no connection or issue with the victim whatsoever.",
                    "Says he was actually planning to invite the victim to co-host future events."
                ],
                clues={
                    "Mess Hall & Campfire": [
                        "A dropped baseball cap with 'QUEST HOST' embroidered on it.",
                        "A pair of broken prescription glasses frames dusted in ash."
                    ],
                    "The Tent Grid": [
                        "Size 11 sneaker prints coated in pine cologne residue.",
                        "A metal cap pin dropped outside the victim's tent entrance."
                    ],
                    "Outer Woods & Ridge": [
                        "A lost compass wrapped in a lanyard bearing Greg's initials.",
                        "A discarded soda can smelling strongly of Greg's cologne."
                    ],
                    "Boathouse & Docks": [
                        "Footprints heading to the dock with wood ash on the soles.",
                        "A spare cap key ring left hanging on a boat cleat."
                    ]
                }
            ),
            Suspect(
                name="Lorelei",
                role="Victim's Sister",
                look="Blonde with sharp blue eyes and highly expressive facial gestures.",
                style="2000s Y2K aesthetics, pink metallic jacket, platform boots, and butterfly hair clips.",
                quirk="Twirls a strand of hair around her finger whenever asked a direct question.",
                true_alibis=[
                    "I was reading inside my tent and only stepped out after the scream.",
                    "I was organizing my fashion wardrobe inside my tent alone.",
                    "I was listening to music on my headphones by the tent clearing."
                ],
                fake_alibis=[
                    "I was at the campfire with Greg drinking hot cocoa.",
                    "I was taking night photos near the boathouse dock.",
                    "I was walking along the woods path looking for stars."
                ],
                true_motives=[
                    "Stood to inherit the victim's rare vintage Y2K fashion collection.",
                    "Was bitter that the victim borrowed her favorite outfit and ruined it.",
                    "Felt the victim was constantly overshadowing her."
                ],
                fake_motives=[
                    "Insists she and the victim were on perfect terms all evening.",
                    "Claims she spent the whole day helping her sister pack her wardrobe."
                ],
                clues={
                    "Mess Hall & Campfire": [
                        "A dropped Y2K pink beaded bracelet near the woodpile.",
                        "A spilled container of glittery strawberry lip-gloss."
                    ],
                    "The Tent Grid": [
                        "A metallic silver shoulder bag snagged on a tent rope.",
                        "Frayed blonde hair strands caught in the victim's tent zipper."
                    ],
                    "Outer Woods & Ridge": [
                        "High-heeled Y2K platform shoe impressions in damp mud.",
                        "A pink butterfly hair clip snagged on low pine needles."
                    ],
                    "Boathouse & Docks": [
                        "A silk scarf printed with a 2000s pattern damp from water.",
                        "A bedazzled compact mirror dropped near the canoe racks."
                    ]
                }
            ),
            Suspect(
                name="Milo",
                role="Group Optimist",
                look="Athletic build with flowy layered brown hair and dark brown eyes.",
                style="Heavy camouflage jacket trimmed with synthetic fur, combat boots, and a holster belt.",
                quirk="Flips a brass hunting coin repeatedly between his knuckles.",
                true_alibis=[
                    "I was out hunting game deep in the woods along the ridge.",
                    "I was checking animal traps near the forest boundary.",
                    "I was hiking up to lookout rock to check night weather."
                ],
                fake_alibis=[
                    "I was in my tent asleep soundly by 9 PM.",
                    "I was hanging out at the mess hall kitchen helping clean up.",
                    "I was stargazing near the main dock by the canoes."
                ],
                true_motives=[
                    "Discovered the victim was spreading rumors to kick him out of camp.",
                    "Believed the victim sabotaged his hunting equipment.",
                    "Got into an argument with the victim over loud late-night noise."
                ],
                fake_motives=[
                    "Claims he barely knew the victim and kept entirely to himself.",
                    "Says he brought the victim an extra blanket earlier that night out of goodwill."
                ],
                clues={
                    "Mess Hall & Campfire": [
                        "A small tuft of synthetic fur from a hood trim on a bench.",
                        "A dropped hunting knife sheath stamped with 'M.O.'"
                    ],
                    "The Tent Grid": [
                        "Heavy fur-lined jacket threads caught on a thorn bush.",
                        "A spent rifle casing smelling freshly of gunpowder."
                    ],
                    "Outer Woods & Ridge": [
                        "A hunting trail marker ribbon torn from Milo's pack.",
                        "Deep combat-boot prints leading toward the ridge overlook."
                    ],
                    "Boathouse & Docks": [
                        "A pocket compass with a cracked lens smelling of fur-wax.",
                        "A trail-mix wrapper torn from Milo's favorite brand."
                    ]
                }
            )
        ]

        # Select Culprit
        self.culprit = random.choice(self.suspects)
        
        # Configure lying behavior based on difficulty
        # Easy: Only culprit lies (30% chance). Innocent suspects tell the truth.
        # Medium: Culprit always lies. Innocents have a 30% chance to lie.
        # Hard: Everyone can lie freely!
        for s in self.suspects:
            if self.difficulty == "Easy":
                s.randomize_round_state(force_lie=(s == self.culprit), lie_chance=0.0)
            elif self.difficulty == "Medium":
                s.randomize_round_state(force_lie=(s == self.culprit), lie_chance=0.3)
            else:  # Hard
                s.randomize_round_state(force_lie=False, lie_chance=0.6)

        self.culprit_location = random.choice(self.locations)
        self.real_clue = random.choice(self.culprit.clues[self.culprit_location])

        innocent_suspects = [s for s in self.suspects if s != self.culprit]
        red_herring_suspect = random.choice(innocent_suspects)
        self.red_herring_location = random.choice(self.locations)
        self.red_herring_clue = random.choice(red_herring_suspect.clues[self.red_herring_location])

    # --- PERFECT ALIGNED HEADER & EXPANDED SUSPECT CARDS ---
    def render_header(self):
        c = Color.CYAN
        print(f"{c}┌{'─' * (BOX_WIDTH + 2)}┐{Color.RESET}")
        print(render_box_line(f"{Color.BOLD}{Color.YELLOW}CAMPSITE MYSTERY: WHO COMMITTED THE CRIME?{Color.RESET}", c))
        print(f"{c}├{'─' * (BOX_WIDTH + 2)}┤{Color.RESET}")
        
        diff_color = Color.GREEN if self.difficulty == "Easy" else (Color.YELLOW if self.difficulty == "Medium" else Color.RED)
        l1 = f"Mode: {diff_color}{self.difficulty}{Color.RESET}   | Rank: {Color.BOLD}{self.stats.rank}{Color.RESET}   | Score: {Color.CYAN}{self.stats.score}{Color.RESET}"
        l2 = f"Streak: {Color.GREEN}{self.stats.win_streak}{Color.RESET}  | Accuracy: {Color.YELLOW}{self.stats.accuracy:.1f}%{Color.RESET}  | Cases: {self.stats.total_cases}"
        
        print(render_box_line(l1, c))
        print(render_box_line(l2, c))
        print(f"{c}└{'─' * (BOX_WIDTH + 2)}┘{Color.RESET}\n")

    def render_suspect_cards(self):
        print(f"{Color.BOLD}{Color.WHITE}── SUSPECT LINEUP ──────────────────────────────────────────────────{Color.RESET}\n")
        for i, suspect in enumerate(self.suspects, 1):
            color = [Color.GREEN, Color.MAGENTA, Color.CYAN][i - 1]
            title_str = f"[{i}] {suspect.name.upper()} ({suspect.role})"
            
            dashes = max(0, BOX_WIDTH - len(title_str) - 3)
            print(f"{color}┌─ {title_str} {'─' * dashes}┐{Color.RESET}")
            
            def print_field(label, text):
                wrapped = textwrap.wrap(f"{label}: {text}", width=BOX_WIDTH - 2)
                # Apply bold formatting to the field label
                label_prefix = f"{Color.BOLD}{label}:{Color.RESET}"
                content = wrapped[0][len(label)+1:]
                print(render_box_line(f"{label_prefix}{content}", color))
                for extra in wrapped[1:]:
                    print(render_box_line(f"   {extra}", color))

            print_field("Look", suspect.look)
            print_field("Style", suspect.style)
            print_field("Quirk", suspect.quirk)
            print_field("Vibe", suspect.current_vibe)
                
            print(f"{color}└{'─' * (BOX_WIDTH + 2)}┘{Color.RESET}\n")

    # --- LOCATION SEARCH ---
    def investigate_locations_menu(self):
        while True:
            clear_screen()
            self.render_header()
            print(f"{Color.BOLD}{Color.YELLOW}=== CRIME SCENE LOCATIONS ==={Color.RESET}\n")
            
            for i, loc in enumerate(self.locations, 1):
                visited_tag = f"{Color.GREEN}(Searched){Color.RESET}" if loc in self.visited_locations else f"{Color.DIM}(Unsearched){Color.RESET}"
                print(f"  [{i}] {loc:<25} {visited_tag}")
            print("  [5] Back to Action Menu\n")

            choice = input(f"{Color.YELLOW}Select location to search (1-5): {Color.RESET}").strip()
            if choice in ["1", "2", "3", "4"]:
                idx = int(choice) - 1
                self.search_location(self.locations[idx])
            elif choice == "5":
                break
            else:
                print(f"{Color.RED}Invalid location selection.{Color.RESET}")
                time.sleep(0.8)

    def search_location(self, loc_name):
        clear_screen()
        self.render_header()
        self.visited_locations.add(loc_name)
        
        print(f"{Color.BOLD}{Color.CYAN}Searching: {loc_name}...{Color.RESET}\n")
        Sound.clue_reveal()
        time.sleep(0.4)

        found_any = False

        if loc_name == self.culprit_location:
            print(f"{Color.YELLOW}┌── EVIDENCE FOUND {'─' * (BOX_WIDTH - 15)}┐{Color.RESET}")
            wrapped_clue = textwrap.wrap(self.real_clue, width=BOX_WIDTH - 2)
            for line in wrapped_clue:
                clue_str = f"{Color.RED}{Color.BOLD}{line}{Color.RESET}"
                print(render_box_line(clue_str, Color.YELLOW))
            print(f"{Color.YELLOW}└{'─' * (BOX_WIDTH + 2)}┘{Color.RESET}\n")
            found_any = True

        if self.difficulty in ["Medium", "Hard"] and loc_name == self.red_herring_location:
            print(f"{Color.MAGENTA}┌── TRACE EVIDENCE (POSSIBLE RED HERRING) {'─' * (BOX_WIDTH - 38)}┐{Color.RESET}")
            wrapped_red = textwrap.wrap(self.red_herring_clue, width=BOX_WIDTH - 2)
            for line in wrapped_red:
                red_str = f"{Color.MAGENTA}{line}{Color.RESET}"
                print(render_box_line(red_str, Color.MAGENTA))
            print(f"{Color.MAGENTA}└{'─' * (BOX_WIDTH + 2)}┘{Color.RESET}\n")
            found_any = True

        if not found_any:
            print(f"{Color.DIM}You searched {loc_name} thoroughly, but found no notable clues here.{Color.RESET}\n")

        input(f"{Color.DIM}Press Enter to return to location list...{Color.RESET}")

    # --- INTERROGATION ---
    def interrogate_menu(self):
        while True:
            clear_screen()
            self.render_header()
            print(f"{Color.BOLD}{Color.CYAN}=== INTERROGATION ROOM ==={Color.RESET}\n")
            for i, suspect in enumerate(self.suspects, 1):
                print(f"  [{i}] Interrogate {suspect.name}")
            print("  [4] Return to Action Menu\n")

            choice = input(f"{Color.YELLOW}Select suspect to interrogate (1-4): {Color.RESET}").strip()
            if choice in ["1", "2", "3"]:
                self.interrogate_suspect(self.suspects[int(choice) - 1])
            elif choice == "4":
                break
            else:
                print(f"{Color.RED}Invalid option.{Color.RESET}")
                time.sleep(0.8)

    def interrogate_suspect(self, suspect):
        clear_screen()
        self.render_header()
        self.interrogation_count += 1
        
        print(f"{Color.BOLD}{Color.CYAN}--- Questioning {suspect.name} ---{Color.RESET}\n")
        print("  [1] Ask about Alibi")
        print("  [2] Investigate Motive")
        print("  [3] Back\n")

        sub_choice = input(f"{Color.YELLOW}Choose line of questioning: {Color.RESET}").strip()
        print()

        if sub_choice == "1":
            # Suspect provides a fake alibi if they are lying in this round
            if suspect.is_lying:
                alibi_text = random.choice(suspect.fake_alibis)
            else:
                alibi_text = random.choice(suspect.true_alibis)
            
            type_writer(f"{Color.BOLD}{suspect.name}:{Color.RESET} \"{alibi_text}\"")
            Sound.clue_reveal()
            input(f"\n{Color.DIM}Press Enter to continue...{Color.RESET}")

        elif sub_choice == "2":
            # Suspect provides a misleading motive statement if lying
            if suspect.is_lying:
                selected_motive = random.choice(suspect.fake_motives)
            else:
                selected_motive = random.choice(suspect.true_motives)

            type_writer(f"{Color.BOLD}Detective Note:{Color.RESET} {suspect.name}'s motive statement: {selected_motive}")
            Sound.clue_reveal()
            input(f"\n{Color.DIM}Press Enter to continue...{Color.RESET}")

    def evaluate_accusal(self, choice_str):
        choice_str = choice_str.strip().lower()
        chosen_suspect = None

        if choice_str.isdigit():
            idx = int(choice_str) - 1
            if 0 <= idx < len(self.suspects):
                chosen_suspect = self.suspects[idx]
        else:
            for suspect in self.suspects:
                if choice_str == suspect.name.lower():
                    chosen_suspect = suspect
                    break

        if not chosen_suspect:
            return None

        is_correct = (chosen_suspect == self.culprit)
        
        if is_correct:
            base_points = 200 if self.difficulty == "Hard" else (150 if self.difficulty == "Medium" else 100)
            deduction = self.interrogation_count * 15
            round_score = max(50, base_points - deduction)
            
            self.stats.cases_solved += 1
            self.stats.win_streak += 1
            self.stats.score += round_score
            Sound.case_solved()
        else:
            self.stats.cases_failed += 1
            self.stats.win_streak = 0
            Sound.case_failed()

        return is_correct, chosen_suspect, self.culprit


# --- DIFFICULTY SELECTION MENU ---
def select_difficulty():
    clear_screen()
    c = Color.CYAN
    print(f"{c}┌{'─' * (BOX_WIDTH + 2)}┐{Color.RESET}")
    print(render_box_line(f"{Color.BOLD}{Color.YELLOW}SELECT INVESTIGATION DIFFICULTY{Color.RESET}", c))
    print(f"{c}└{'─' * (BOX_WIDTH + 2)}┘{Color.RESET}\n")
    print(f"  {Color.GREEN}[1] Easy{Color.RESET}   - 1 clear clue. Innocent suspects tell the truth.")
    print(f"  {Color.YELLOW}[2] Medium{Color.RESET} - Red herrings present. Culprit lies; innocents may lie.")
    print(f"  {Color.RED}[3] Hard{Color.RESET}   - Red herrings present. High chance ANY suspect lies!\n")

    while True:
        choice = input(f"{Color.BOLD}Choose Difficulty (1-3): {Color.RESET}").strip()
        if choice == "1":
            return "Easy"
        elif choice == "2":
            return "Medium"
        elif choice == "3":
            return "Hard"
        else:
            print(f"{Color.RED}Invalid selection. Pick 1, 2, or 3.{Color.RESET}")


# --- MAIN GAME LOOP ---
def main():
    stats = DetectiveStats()

    while True:
        difficulty = select_difficulty()
        game = Mystery(difficulty, stats)

        while True:
            clear_screen()
            game.render_header()
            game.render_suspect_cards()

            print(f"{Color.BOLD}{Color.WHITE}── ACTIONS ─────────────────────────────────────────────────────────{Color.RESET}")
            print("  [1-3 or Name] Accuse Suspect")
            print("  [L] Search Campsite Locations")
            print("  [I] Interrogate Suspects")
            print("  [Q] Quit Game\n")

            user_input = input(f"{Color.BOLD}{Color.YELLOW}Select Action: {Color.RESET}").strip()

            if user_input.lower() == 'l':
                game.investigate_locations_menu()
            elif user_input.lower() == 'i':
                game.interrogate_menu()
            elif user_input.lower() == 'q':
                clear_screen()
                print(f"\n{Color.CYAN}Thanks for playing Campsite Mystery! Good luck out there, Detective.{Color.RESET}\n")
                return
            else:
                result = game.evaluate_accusal(user_input)
                if result is not None:
                    is_correct, chosen, culprit = result
                    
                    print("\n" + f"{Color.CYAN}═" * (BOX_WIDTH + 4) + f"{Color.RESET}")
                    if is_correct:
                        print(f"{Color.BG_GREEN}{Color.WHITE}{Color.BOLD} CASE SOLVED! {Color.RESET} {Color.GREEN}You correctly identified {chosen.name} as the culprit!{Color.RESET}")
                    else:
                        print(f"{Color.BG_RED}{Color.WHITE}{Color.BOLD} CASE FAILED! {Color.RESET} {Color.RED}{chosen.name} is innocent. The real culprit was {culprit.name}!{Color.RESET}")
                    print(f"{Color.CYAN}═" * (BOX_WIDTH + 4) + f"{Color.RESET}\n")
                    
                    input(f"{Color.DIM}Press Enter to continue to next case...{Color.RESET}")
                    break
                else:
                    print(f"{Color.RED}Invalid selection. Type 1-3, suspect name, 'L', or 'I'.{Color.RESET}")
                    time.sleep(1)


if __name__ == "__main__":
    main()