import random
from datetime import datetime

# ── Supporting data ──────────────────────────────────────────────────────────

INDUCTION_CENTERS = [
    ("Fort Campbell, Kentucky", "the 101st Airborne Division"),
    ("Fort Benning, Georgia", "the Infantry Training Brigade"),
    ("Fort Bragg, North Carolina", "the 82nd Airborne Division"),
    ("Fort Dix, New Jersey", "the 2nd Training Brigade"),
    ("Fort Jackson, South Carolina", "the 1st Training Brigade"),
    ("Fort Knox, Kentucky", "the Armor Center"),
    ("Fort Lewis, Washington", "the 9th Infantry Division"),
    ("Fort Ord, California", "the 7th Infantry Division"),
    ("Fort Polk, Louisiana", "the 5th Infantry Division"),
]

DEPLOYMENT_LOCATIONS = [
    {
        "location": "the Mekong Delta",
        "province": "III Corps Tactical Zone",
        "unit": "9th Infantry Division",
        "description": "a maze of rivers, rice paddies, and mangrove forests where the Viet Cong moved like shadows through the waterways.",
        "danger": "high"
    },
    {
        "location": "the Central Highlands",
        "province": "II Corps Tactical Zone",
        "unit": "4th Infantry Division",
        "description": "rugged mountain terrain blanketed in triple-canopy jungle where the Ho Chi Minh Trail fed men and materiel south.",
        "danger": "very high"
    },
    {
        "location": "the DMZ",
        "province": "I Corps Tactical Zone",
        "unit": "3rd Marine Division",
        "description": "the demilitarized zone along the 17th parallel — the most contested and deadly stretch of ground in all of Vietnam.",
        "danger": "extreme"
    },
    {
        "location": "Quảng Trị Province",
        "province": "I Corps Tactical Zone",
        "unit": "101st Airborne Division",
        "description": "fiercely contested northern territory where the ghosts of Khe Sanh and Hamburger Hill still lingered.",
        "danger": "very high"
    },
    {
        "location": "Biên Hòa Province",
        "province": "III Corps Tactical Zone",
        "unit": "1st Infantry Division",
        "description": "the heartland of the war, home to massive American bases and the ever-present threat of rocket and mortar attacks.",
        "danger": "moderate"
    },
    {
        "location": "the Iron Triangle",
        "province": "III Corps Tactical Zone",
        "unit": "25th Infantry Division",
        "description": "a 60-square-mile Viet Cong stronghold of tunnels, booby traps, and hidden bunkers just 25 miles from Saigon.",
        "danger": "high"
    },
    {
        "location": "the A Shau Valley",
        "province": "I Corps Tactical Zone",
        "unit": "101st Airborne Division",
        "description": "a remote valley bordering Laos, one of the most dangerous corridors of the entire war — a place men whispered about.",
        "danger": "extreme"
    },
    {
        "location": "the Saigon perimeter",
        "province": "III Corps Tactical Zone",
        "unit": "199th Infantry Brigade",
        "description": "the ring of firebases and checkpoints surrounding the capital, always alert after the shock of the Tet Offensive.",
        "danger": "moderate"
    },
]

MOS_ROLES = [
    ("11B", "Infantryman", "the sharp end of the spear — carrying an M16 through jungle and paddies, often the first to make contact with the enemy"),
    ("11C", "Indirect Fire Infantryman", "an 81mm mortar crew member, providing fire support to troops in contact across broken terrain"),
    ("13F", "Fire Support Specialist", "calling in artillery strikes from forward positions, often under fire yourself while giving grid coordinates over the radio"),
    ("12B", "Combat Engineer", "clearing mines and booby traps — work that demanded steady hands and nerves of steel, every single day"),
    ("91B", "Combat Medic", "the platoon's lifeline, running to the wounded under fire with nothing but a Unit One medical kit and sheer courage"),
    ("05B", "Radio Operator", "carrying the heavy PRC-25 'Prick' radio through the bush, ensuring the platoon never lost contact with command"),
    ("64C", "Motor Transport Operator", "hauling supplies and troops on roads that could become killing grounds at any bend"),
    ("96B", "Intelligence Analyst", "piecing together enemy movements from captured documents, interrogations, and aerial reconnaissance"),
]

PHYSICAL_EXAM_LOCATIONS = [
    "AFEES Chicago (Van Buren St)",
    "AFEES Los Angeles (Western Ave)",
    "AFEES New York (Whitehall Street)",
    "AFEES Houston (San Jacinto St)",
    "AFEES Detroit (Mount Elliott St)",
    "AFEES Philadelphia (North Broad St)",
    "AFEES Atlanta (Ponce de Leon Ave)",
    "AFEES Seattle (Second Ave)",
    "AFEES Boston (Fargo St)",
    "AFEES Dallas (Main St)",
    "AFEES Denver (Stout St)",
    "AFEES Memphis (North Main St)",
]


def get_season(month: int) -> str:
    if month in [12, 1, 2]:
        return "winter"
    elif month in [3, 4, 5]:
        return "spring"
    elif month in [6, 7, 8]:
        return "summer"
    else:
        return "fall"


def get_zodiac(month: int, day: int) -> str:
    # Each tuple: (Month, Day the sign ENDS, The sign for the first half of the month)
    signs = [
        (1, 19, "Capricorn"), (2, 18, "Aquarius"), (3, 20, "Pisces"),
        (4, 19, "Aries"), (5, 20, "Taurus"), (6, 20, "Gemini"),
        (7, 22, "Cancer"), (8, 22, "Leo"), (9, 22, "Virgo"),
        (10, 22, "Libra"), (11, 21, "Scorpio"), (12, 21, "Sagittarius"),
    ]
    
    for m, d, sign in signs:
        if month == m:
            if day <= d:
                return sign
            else:
                # If it's after the end date, return the next sign in the cycle
                idx = [s[2] for s in signs].index(sign)
                return signs[(idx + 1) % 12][2]
                
    return "Capricorn"

def seed_from_date(month: int, day: int, year: int) -> int:
    # Generates a unique integer like 11112026 for Nov 11, 2026
    return month * 1000000 + day * 10000 + year


# ── Main story function ──────────────────────────────────────────────────────

def generate_draft_story(month: int, day: int, year: int, draft_number: int, was_drafted: bool) -> str:
    rng = random.Random(seed_from_date(month, day, year))

    month_name = datetime(2000, month, 1).strftime("%B")
    season = get_season(month)
    zodiac = get_zodiac(month, day)

    induction_city, division = rng.choice(INDUCTION_CENTERS)
    exam_city = rng.choice(PHYSICAL_EXAM_LOCATIONS)
    deployment = rng.choice(DEPLOYMENT_LOCATIONS)
    mos_code, mos_title, mos_desc = rng.choice(MOS_ROLES)
    birth_year_low = year - 26
    birth_year_high = year - 18

    notice_weeks = rng.randint(3, 8)
    training_weeks = rng.randint(8, 16)

    if was_drafted:
        story = _drafted_story(
            month_name, day, year, season, zodiac,
            draft_number, induction_city, division, exam_city,
            deployment, mos_code, mos_title, mos_desc,
            notice_weeks, training_weeks,
            birth_year_low, birth_year_high, rng
        )
    else:
        story = _safe_story(
            month_name, day, year, season, zodiac,
            draft_number, exam_city,
            birth_year_low, birth_year_high, rng
        )

    return story


def _drafted_story(
    month_name, day, year, season, zodiac,
    draft_number, induction_city, division, exam_city,
    deployment, mos_code, mos_title, mos_desc,
    notice_weeks, training_weeks,
    birth_year_low, birth_year_high, rng
) -> str:

    lottery_month = "December" if year == 1969 else "July" if year == 1970 else "August" if year == 1971 else "February"
    lottery_year_prev = year - 1 if year == 1969 else year

    opening_lines = [
        f"It was a {season} morning when the envelope arrived.",
        f"The letter came on a Tuesday — ordinary enough until you saw the return address.",
        f"You were born on {month_name} {day} — a {season} birthday. That date would define your life.",
        f"Some birthdays feel like a gift. This one was drawn from a capsule in Washington.",
    ]
    opening = rng.choice(opening_lines)

    paragraphs = []

    # Para 1: The lottery night
    paragraphs.append(
        f"{opening} On {lottery_month} 1, {lottery_year_prev if year == 1969 else year}, "
        f"officials at Selective Service headquarters in Washington D.C. reached into a glass bowl "
        f"and drew blue plastic capsules — each one a birthday, each one a fate. "
        f"Your birthday, {month_name} {day}, came out as number <strong>{draft_number}</strong>. "
        f"In a lottery of 365 numbers, yours fell within the range that would be called."
    )

    # Para 2: The notice
    paragraphs.append(
        f"The official induction notice arrived roughly {notice_weeks} weeks later. "
        f"It read: <em>\"Greeting: You are hereby ordered for induction into the Armed Forces of the United States.\"</em> "
        f"You were to report for a pre-induction physical examination to {exam_city}. "
        f"The exam took a full day — vision, hearing, blood pressure, a battery of tests designed to determine "
        f"if your body was fit for the demands of war. Yours was."
    )

    # Para 3: Basic training
    paragraphs.append(
        f"From there, you were assigned to {induction_city}, home of {division}. "
        f"Basic Combat Training lasted {training_weeks} weeks — a controlled demolition of the civilian you used to be. "
        f"Reveille at 0430. Five-mile runs in the Georgia heat. Weapons familiarization, land navigation, "
        f"first aid under simulated fire. Drill Sergeants who seemed to have been carved from the same hard rock "
        f"as the obstacle courses they built. By the end, you were different. Most men were."
    )

    # Para 4: MOS and assignment
    paragraphs.append(
        f"Your Military Occupational Specialty was assessed as <strong>{mos_code} — {mos_title}</strong>: "
        f"{mos_desc}. Orders came down shortly after Advanced Individual Training. "
        f"You were being sent to Vietnam — specifically to {deployment['location']}, "
        f"{deployment['province']}, attached to the <strong>{deployment['unit']}</strong>."
    )

    # Para 5: The place
    paragraphs.append(
        f"Those who'd been there before said {deployment['location']} was {deployment['description']} "
        f"The threat level was assessed as <strong>{deployment['danger']}</strong>. "
        f"You would serve a standard 365-day tour — if things went as planned. "
        f"You wrote letters home. You learned to sleep with one ear open. "
        f"You learned the names of the men beside you faster than you'd ever learned anything in school."
    )

    # Para 6: Closing / reflection
    closings = [
        f"Of the approximately 2.7 million Americans who served in Vietnam, "
        f"58,220 did not come home. Whether you were among the fortunate or the fallen "
        f"is a story only history knows. What is certain: your number came up, "
        f"and like so many young men born in {season}, you answered.",

        f"The war would end on April 30, 1975 — but for the men who served, "
        f"it never fully ended. You were one of them. Born on {month_name} {day}, "
        f"a Zodiac sign of {zodiac}, drafted in {year}. Your country called. You went.",

        f"One in three men who served in Vietnam was a draftee. You would have been one of them — "
        f"a young man who didn't choose this war, but served it anyway. "
        f"History is full of people like you. Most of them never got a monument.",
    ]
    paragraphs.append(rng.choice(closings))

    return "<br><br>".join(paragraphs)


def _safe_story(
    month_name, day, year, season, zodiac,
    draft_number, exam_city,
    birth_year_low, birth_year_high, rng
) -> str:

    lottery_month = "December" if year == 1969 else "July" if year == 1970 else "August" if year == 1971 else "February"
    lottery_year_prev = year - 1 if year == 1969 else year

    thresholds = {1969: 195, 1970: 195, 1971: 125, 1972: 95}
    threshold = thresholds[year]

    paragraphs = []

    openings = [
        f"You were born on {month_name} {day} — a {season} birthday. The capsule with your date was drawn.",
        f"The lottery was held on {lottery_month} 1{', ' + str(lottery_year_prev) if year == 1969 else ', ' + str(year)}. Every birthday had a number. Yours came up.",
        f"On {lottery_month} of that year, your birthday was pulled from a bowl in Washington. It had a number attached.",
    ]
    paragraphs.append(rng.choice(openings))

    # Para 2: the number
    paragraphs.append(
        f"Your lottery number was <strong>{draft_number}</strong>. "
        f"In the {year} lottery, the Selective Service called numbers <strong>1 through {threshold}</strong>. "
        f"Your number fell above that line. You were not inducted."
    )

    # Para 3: what that meant
    wait_descriptions = [
        f"Men with your number received no notice, no physical exam, no orders. "
        f"You watched the news like everyone else — the body counts, the protests on college campuses, "
        f"the flags folded at funerals in your town. You waited for a letter that never came.",

        f"The Selective Service processed lower numbers first. Yours was high enough that the quota was filled "
        f"before they reached you. There was no ceremony marking your escape — just the slow realization, "
        f"weeks later, that the envelope wasn't coming.",

        f"You may not have even known for weeks. Men checked newspapers, called their draft boards, waited. "
        f"Eventually the word filtered through: the calls had stopped. Your number was too high.",
    ]
    paragraphs.append(rng.choice(wait_descriptions))

    # Para 4: life around you
    paragraphs.append(
        f"But the war was still there. Neighbors shipped out. Classmates didn't come back. "
        f"The evening news put the casualty figures in the same breath as the weather. "
        f"Being spared the draft didn't spare you from living through the era — the assassinations, "
        f"the marches, the fractures running through the country like fault lines. "
        f"Vietnam shaped a generation whether you served or not."
    )

    # Para 5: closing
    closings = [
        f"Your birthday — {month_name} {day}, lottery number {draft_number} — was a number that let you stay. "
        f"58,220 other Americans were not as fortunate. "
        f"The lottery was random, impersonal, and absolute. Luck of the draw. Literally.",

        f"You were born a {zodiac}. You were born in {season}. You were born with a number that kept you home. "
        f"History is full of such accidents — small numerical differences that meant everything.",

        f"The men who went called it 'the green machine.' Those who stayed behind called it survival. "
        f"Your number was {draft_number}. The cutoff was {threshold}. "
        f"Six digits of difference — that's what stood between you and a jungle 10,000 miles away.",
    ]
    paragraphs.append(rng.choice(closings))

    return "<br><br>".join(paragraphs)
