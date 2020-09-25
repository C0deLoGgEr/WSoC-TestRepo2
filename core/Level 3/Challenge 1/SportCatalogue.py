import abc  # abc stabds for Abstract Base Class. This package is used to implement abstract classes.


class Sport(metaclass=abc.ABCMeta):
    def __init__(self, name, nop, time, origin, hasSubgame, equipments, legend_name, legend_origin, isLegendPlaying):
        self.name = name
        self.nop = nop
        self.time = time
        self.origin = origin
        self.hasSubgame = hasSubgame
        self.equipments = equipments
        self.legend_name = legend_name
        self.legend_origin = legend_origin
        self.isLegendPlaying = isLegendPlaying
        self.getProperties()
        self.getBriefInfo()

    @abc.abstractmethod
    def getBriefInfo(self):
        pass

    def getProperties(self):
        print(f""" 
                   ABOUT GAME 
                   ==========
                   Sport Name: {self.name} 
                   Players Required (Minimum/Exact): {self.nop}
                   Time Duration (Minimum/Exact): {self.time}
                   Origin: {self.origin}
                   Has Different Types of Subgames?: {"Yes" if self.hasSubgame else "No"}
                   Basic Equipments Required: {self.equipments}

                   ABOUT BEST PLAYER
                   =================
                   Player Name: {self.legend_name}
                   Player Origin: {self.legend_origin}
                   Player Serving: {"Yes!!" if self.isLegendPlaying else "No, Currently Retired :("}
""")


class Boxing(Sport):
    def __init__(self, name, nop, time, origin, hasSubgame, equipments, legend_name, legend_origin, isLegendPlaying):
        super().__init__(name, nop, time, origin, hasSubgame, equipments, legend_name, legend_origin, isLegendPlaying)

    def getBriefInfo(self):
        print(""" 
                  << MORE INFO ON BOXING >>
                  --------------------------------------------
                  Boxing is a combat sport in which two people, usually wearing protective gloves, throw
                  punches at each other for a predetermined amount of time in a boxing ring. A winner can be
                  resolved before the completion of the rounds when a referee deems an opponent incapable of
                  continuing, disqualification of an opponent, or resignation of an opponent. When the fight reaches
                  the end of its final round with both opponents still standing, the judges' scorecards determine
                  the victor. In the event that both fighters gain equal scores from the judges, professional bouts
                  are considered a draw. A boxing match typically consists of a determined number of three-minute
                  rounds, a total of up to 9 to 12 rounds. """)


class Chess(Sport):
    def __init__(self, name, nop, time, origin, hasSubgame, equipments, legend_name, legend_origin, isLegendPlaying):
        super().__init__(name, nop, time, origin, hasSubgame, equipments, legend_name, legend_origin, isLegendPlaying)

    def getBriefInfo(self):
        print(""" 
                  << MORE INFO ON CHESS >>
                  --------------------------------------------
                  Chess is a two-player strategy board game played on a checkered board with 64 squares 
                  arranged in an 8×8 square grid. Played by millions of people worldwide, chess is believed to be 
                  derived from the Indian game chaturanga sometime before the 7th century. Each player begins with 
                  16 pieces: one king, one queen, two rooks, two knights, two bishops, and eight pawns. Each piece
                  type moves differently, with the most powerful being the queen and the least powerful the pawn. 
                  The objective is to checkmate the opponent's king by placing it under an inescapable threat of 
                  capture.To this end, a player's pieces are used to attack and capture the opponent's pieces, while 
                  supporting one another. During the game, play typically involves exchanging pieces for the 
                  opponent's similar pieces, and finding and engineering opportunities to trade advantageously or to
                  get a better position. In addition to checkmate, a player wins the game if the opponent resigns,
                  or, in a timed game, runs out of time. There are also several ways that a game can end in a draw.
                  Sometimes Chess Tournaments may take upto 6 hours.
                   """)


class TableTennis(Sport):
    def __init__(self, name, nop, time, origin, hasSubgame, equipments, legend_name, legend_origin, isLegendPlaying):
        super().__init__(name, nop, time, origin, hasSubgame, equipments, legend_name, legend_origin, isLegendPlaying)

    def getBriefInfo(self):
        print(""" 
                  << MORE INFO ON TABLE-TENNIS >>
                  --------------------------------------------
                  Table tennis, also known as ping-pong and whiff-whaff, is a sport in which two or four
                  players hit a lightweight ball, also known as the ping-pong ball, back and forth across a table 
                  using small rackets. The game takes place on a hard table divided by a net. Except for the initial
                  serve, the rules are generally as follows: players must allow a ball played toward them to bounce 
                  one time on their side of the table, and must return it so that it bounces on the opposite side at
                  least once. A point is scored when a player fails to return the ball within the rules. Play is 
                  fast and demands quick reactions. Spinning the ball alters its trajectory and limits an opponent's 
                  options, giving the hitter a great advantage.
                   """)


class Cricket(Sport):
    def __init__(self, name, nop, time, origin, hasSubgame, equipments, legend_name, legend_origin, isLegendPlaying):
        super().__init__(name, nop, time, origin, hasSubgame, equipments, legend_name, legend_origin, isLegendPlaying)
        self.getAbout_test()
        self.getAbout_odi()
        self.getAbout_t20()

    def getBriefInfo(self):
        print(""" 
                  << MORE INFO ON CRICKET >>
                  --------------------------------------------
                  Cricket is a bat-and-ball game played between two teams of eleven players on a field at
                  the centre of which is a 22-yard (20-metre) pitch with a wicket at each end, each comprising two
                  bails balanced on three stumps. The batting side scores runs by striking the ball bowled at the
                  wicket with the bat (and running between the wickets), while the bowling and fielding side tries
                  to prevent this (by getting the ball to either wicket) and dismiss each batter (so they are out).
                  Means of dismissal include being bowled, when the ball hits the stumps and dislodges the bails, 
                  and by the fielding side catching the ball after it is hit by the bat, but before it hits the 
                  ground. When ten batters have been dismissed, the innings ends and the teams swap roles. The game
                  is adjudicated by two umpires, aided by a third umpire and match referee in international matches.
                   """)

    def getAbout_odi(self):
        print("""
                  << (SUBGAME)=> ONE DAY CRICKET MATCHES >>
                  --------------------------------------------
                  The shorter version of cricket is called One Day match: Invented in 1970’s, each
                  match consists of 50 overs being played by each side and the team scoring more runs in their quota
                  of 50 overs wins. A team is normally given 3 hrs 30 mins of time to bowl its quota of 50 overs
                  plus there is a break of 40 to 45 mins between the two innings so the game lasts for ~ 8 hours.
        """)

    def getAbout_t20(self):
        print("""
                  << (SUBGAME)=> T20 CRICKET MATCHES >>
                  --------------------------------------------
                  The most recent & shortest format is called Twenty-twenty or T20: Here each team gets
                  to bat 20 overs and the team scoring more in their allotted 20 overs wins. A typical T20 match
                  gets over within 4 hours
        """)

    def getAbout_test(self):
        print("""
                  << (SUBGAME)=> TEST CRICKET MATCHES >>
                  --------------------------------------------
                  The oldest and longest format is called Test Cricket- This is the original form of 
                  cricket invented by the British. It is played over 5 days, minimum 90 overs to be played in each day.
                  ( An over is a span of 6 balls continuously bowled by 1 particular bowler. After bowling an 
                  over, he is replaced by another bowler to bowl another over from the opposite end). Minimum 6
                  hours of play is scheduled for each day. Each team gets to bat twice in a span of 5 days. each slot 
                  is called an inning.
        """)


class Football(Sport):
    def __init__(self, name, nop, time, origin, hasSubgame, equipments, legend_name, legend_origin, isLegendPlaying):
        super().__init__(name, nop, time, origin, hasSubgame, equipments, legend_name, legend_origin, isLegendPlaying)

    def getBriefInfo(self):
        print(""" 
                  << MORE INFO ON FOOTBALL >>
                  --------------------------------------------
                  Football or Soccer, is a team sport played with a spherical ball between two teams 
                  of 11 players. It is played by approximately 250 million players in over 200 countries and 
                  dependencies, making it the world's most popular sport. The game is played on a rectangular field 
                  called a pitch with a goal at each end. The object of the game is to outscore the opposition by 
                  moving the ball beyond the goal line into the opposing goal. The team with the higher number of 
                  goals wins the game. Players are not allowed to touch the ball with hands or arms while it is in 
                  play, except for the goalkeepers within the penalty area. Other players mainly use their feet to 
                  strike or pass the ball, but may also use any other part of their body except the hands and the 
                  arms. The team that scores most goals by the end of the match wins. If the score is level at the
                  end of the game, either a draw is declared or the game goes into extra time or a penalty shootout
                  depending on the format of the competition. """)


class Volleyball(Sport):
    def __init__(self, name, nop, time, origin, hasSubgame, equipments, legend_name, legend_origin, isLegendPlaying):
        super().__init__(name, nop, time, origin, hasSubgame, equipments, legend_name, legend_origin, isLegendPlaying)

    def getBriefInfo(self):
        print(""" 
                  << MORE INFO ON VOLLEYBALL >>
                  --------------------------------------------
                  Volleyball is a team sport in which two teams of six players are separated by a net.
                  Each team tries to score points by grounding a ball on the other team's court under organized 
                  rules. A player on one of the teams begins a 'rally' by serving the ball (tossing or releasing it 
                  and then hitting it with a hand or arm), from behind the back boundary line of the court, over 
                  the net, and into the receiving team's court. The receiving team must not let the ball be grounded
                  within their court. The team may touch the ball up to 3 times, but individual players may not 
                  touch the ball twice consecutively. Typically, the first two touches are used to set up for
                  an attack, an attempt to direct the ball back over the net in such a way that the serving team is
                  unable to prevent it from being grounded in their court. The rally continues, with each team 
                  allowed as many as three consecutive touches, until either a team makes a kill, grounding 
                  the ball on the opponent's court and winning the rally; or a team commits a fault and loses 
                  the rally. The team that wins the rally is awarded a point and serves the ball to start the 
                  next rally. """)


def menu():
    print("""
                 SPORTS CATALOGUE
                 ----------------
                 Indoor Sports: \n\t\t\t\t (1) Boxing \n\t\t\t\t (2) Chess \n\t\t\t\t (3) Table Tennis
                 Outdoor Sports: \n\t\t\t\t (4) Cricket \n\t\t\t\t (5) Football \n\t\t\t\t (6) Volleyball \n\t\t\t (0) Exit
                  """)
    value = input("\t\t\t\tEnter your choice (must be a number):>>")
    return int(value)


while True:
    choice = menu()
    if choice == 1:
        obj = Boxing("Boxing", 2, 30, "Egypt", False, ["Headgear", "Mouth Guard", "Boxing Gloves", "Boxing Mittens",
                                                       "Ankle Supports and Inner Gloves"], "Muhammad Ali", "America",
                     False)
    elif choice == 2:
        obj = Chess("Chess", 2, 60, "India", False, ["Chess Pieces", "Chess Board"],
                    "Sven Magnus Øen Carlsen", "Norway", True)
    elif choice == 3:
        obj = TableTennis("Table Tennis", 2, 10, "England", False,
                          ["Ping-Pong ball", "Table Tennis Racket", "Table"], "Jan-Ove Waldner",
                          "Sweden", False)
    elif choice == 4:
        obj = Cricket("Cricket", 22, 240, "England", True, ["Cricket Bat", "Batting Leg-Guards", "Batting Gloves",
                                                            "Thigh Guard/Lower Body Protector",
                                                            "Abdominal Protector/Box", "Batting Helmet",
                                                            "Cricket Balls, Cricket Stump, Cricket Bails"],
                      "Sachin Tendulkar", "India",
                      False)
    elif choice == 5:
        obj = Football("Football/Soccer", 22, 90, "Ancient China, Greece, Rome and England", False,
                       ["Uniform", "Soccer Cleats", "Shin Guards", "GoalKeeper Gloves", "Ball"],
                       "Cristiano Ronaldo", "Portugal", True)
    elif choice == 6:
        obj = Volleyball("Volleyball", 12, 60, "USA", False, ["Volleyball", "Sport outfit", "Ankle Braces", "Knee Pad"],
                         "Karch Kiraly", "America", False)
    elif choice == 0:
        break

    else:
        print("(COMMAND-LINE)>> Enter a valid input!!")
