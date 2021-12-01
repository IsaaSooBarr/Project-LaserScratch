from Utility.ByteStream import Writer


class SeasonRewardsMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24123
        self.client = client
        self.player = player


    def encode(self):
        StarPointsTrophiesStart = [550,600,650,700,750,800,850,900,950,1000,1050,1100,1150,1200,1250,1300,1350,1400]
        StarPointsTrophiesEnd = [599,649,699,749,799,849,899,949,999,1049,1099,1149,1199,1249,1299,1349,1399,-1]
        StarPointsSeasonRewardAmount = [70,120,160,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480]
        StarPointsTrophiesInReset = [525,550,575,600,625,650,675,700,725,750,775,800,825,850,875,900,925,950]
        self.writeVInt(len(StarPointsTrophiesStart)) # Index Count
        for StarPointsIndex in range(len(StarPointsTrophiesStart)):
            self.writeVInt(StarPointsTrophiesStart[StarPointsIndex]) # Minimum Trophies Index For Season Reward
            self.writeVInt(StarPointsTrophiesEnd[StarPointsIndex]) # Maximum Trophies Index For Season Reward
            self.writeVInt(StarPointsSeasonRewardAmount[StarPointsIndex]) # Season Star Points Reward Amount
            self.writeVInt(StarPointsTrophiesInReset[StarPointsIndex]) # Trophies After Season End