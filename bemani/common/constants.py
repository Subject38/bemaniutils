class GameConstants:
    BISHI_BASHI = 'bishi'
    DANCE_EVOLUTION = 'danevo'
    DDR = 'ddr'
    IIDX = 'iidx'
    JUBEAT = 'jubeat'
    MUSECA = 'museca'
    POPN_MUSIC = 'pnm'
    REFLEC_BEAT = 'reflec'
    SDVX = 'sdvx'


class VersionConstants:
    BISHI_BASHI_TSBB = 1

    DDR_1STMIX = 1
    DDR_2NDMIX = 2
    DDR_3RDMIX = 3
    DDR_4THMIX = 4
    DDR_5THMIX = 5
    DDR_6THMIX = 6
    DDR_7THMIX = 7
    DDR_EXTREME = 8
    DDR_SUPERNOVA = 9
    DDR_SUPERNOVA_2 = 10
    DDR_X = 11
    DDR_X2 = 12
    DDR_X3_VS_2NDMIX = 13
    DDR_2013 = 14
    DDR_2014 = 15
    DDR_ACE = 16
    DDR_A20 = 17

    IIDX = 1
    IIDX_2ND_STYLE = 2
    IIDX_3RD_STYLE = 3
    IIDX_4TH_STYLE = 4
    IIDX_5TH_STYLE = 5
    IIDX_6TH_STYLE = 6
    IIDX_7TH_STYLE = 7
    IIDX_8TH_STYLE = 8
    IIDX_9TH_STYLE = 9
    IIDX_10TH_STYLE = 10
    IIDX_RED = 11
    IIDX_HAPPY_SKY = 12
    IIDX_DISTORTED = 13
    IIDX_GOLD = 14
    IIDX_DJ_TROOPERS = 15
    IIDX_EMPRESS = 16
    IIDX_SIRIUS = 17
    IIDX_RESORT_ANTHEM = 18
    IIDX_LINCLE = 19
    IIDX_TRICORO = 20
    IIDX_SPADA = 21
    IIDX_PENDUAL = 22
    IIDX_COPULA = 23
    IIDX_SINOBUZ = 24
    IIDX_CANNON_BALLERS = 25
    IIDX_ROOTAGE = 26
    IIDX_HEROIC_VERSE = 27
    IIDX_BISTROVER = 28

    JUBEAT = 1
    JUBEAT_RIPPLES = 2
    JUBEAT_RIPPLES_APPEND = 3
    JUBEAT_KNIT = 4
    JUBEAT_KNIT_APPEND = 5
    JUBEAT_COPIOUS = 6
    JUBEAT_COPIOUS_APPEND = 7
    JUBEAT_SAUCER = 8
    JUBEAT_SAUCER_FULFILL = 9
    JUBEAT_PROP = 10
    JUBEAT_QUBELL = 11
    JUBEAT_CLAN = 12
    JUBEAT_FESTO = 13

    MUSECA = 1
    MUSECA_1_PLUS = 2

    POPN_MUSIC = 1
    POPN_MUSIC_2 = 2
    POPN_MUSIC_3 = 3
    POPN_MUSIC_4 = 4
    POPN_MUSIC_5 = 5
    POPN_MUSIC_6 = 6
    POPN_MUSIC_7 = 7
    POPN_MUSIC_8 = 8
    POPN_MUSIC_9 = 9
    POPN_MUSIC_10 = 10
    POPN_MUSIC_11 = 11
    POPN_MUSIC_IROHA = 12
    POPN_MUSIC_CARNIVAL = 13
    POPN_MUSIC_FEVER = 14
    POPN_MUSIC_ADVENTURE = 15
    POPN_MUSIC_PARTY = 16
    POPN_MUSIC_THE_MOVIE = 17
    POPN_MUSIC_SENGOKU_RETSUDEN = 18
    POPN_MUSIC_TUNE_STREET = 19
    POPN_MUSIC_FANTASIA = 20
    POPN_MUSIC_SUNNY_PARK = 21
    POPN_MUSIC_LAPISTORIA = 22
    POPN_MUSIC_ECLALE = 23
    POPN_MUSIC_USANEKO = 24
    POPN_MUSIC_PEACE = 25
    POPN_MUSIC_KAIMEI_RIDDLES = 26

    REFLEC_BEAT = 1
    REFLEC_BEAT_LIMELIGHT = 2
    REFLEC_BEAT_COLETTE = 3
    REFLEC_BEAT_GROOVIN = 4
    REFLEC_BEAT_VOLZZA = 5
    REFLEC_BEAT_VOLZZA_2 = 6
    REFLEC_BEAT_REFLESIA = 7

    SDVX_BOOTH = 1
    SDVX_INFINITE_INFECTION = 2
    SDVX_GRAVITY_WARS = 3
    SDVX_HEAVENLY_HAVEN = 4
    SDVX_VIVID_WAVE = 5


class APIConstants:
    ID_TYPE_SERVER = 'server'
    ID_TYPE_CARD = 'card'
    ID_TYPE_SONG = 'song'
    ID_TYPE_INSTANCE = 'instance'


class DBConstants:
    # When adding new game series, I try to make sure that constants
    # go in order, and have a difference of 100 between them. This is
    # so I can promote lamps/scores/etc by using a simple "max", while
    # still allowing for new game versions to insert new constants anywhere
    # in the lineup. You'll notice a few areas where constants go up by
    # non-100. This is because a new game came out in this series after
    # existing scores were in production, so constants for new grades/lamps
    # had to be snuck in. The actual constant doesn't matter as long as they
    # go in order, so this works out nicely.

    # Its up to various games to map the in-game constant to these DB
    # constants. Most games will implement a pair of functions that takes
    # one of these values and spits out the game-specific constant, and
    # vice versa. This keeps us individual game agnostic and allows us to
    # react easily to renumberings and constant insertions. These constants
    # will only be found in the DB itself, as well as used on the frontend
    # to display various general information about scores.

    OMNIMIX_VERSION_BUMP = 10000

    DDR_HALO_NONE = 100
    DDR_HALO_GOOD_FULL_COMBO = 200
    DDR_HALO_GREAT_FULL_COMBO = 300
    DDR_HALO_PERFECT_FULL_COMBO = 400
    DDR_HALO_MARVELOUS_FULL_COMBO = 500
    DDR_RANK_E = 100
    DDR_RANK_D = 200
    DDR_RANK_D_PLUS = 233
    DDR_RANK_C_MINUS = 266
    DDR_RANK_C = 300
    DDR_RANK_C_PLUS = 333
    DDR_RANK_B_MINUS = 366
    DDR_RANK_B = 400
    DDR_RANK_B_PLUS = 433
    DDR_RANK_A_MINUS = 466
    DDR_RANK_A = 500
    DDR_RANK_A_PLUS = 533
    DDR_RANK_AA_MINUS = 566
    DDR_RANK_AA = 600
    DDR_RANK_AA_PLUS = 650
    DDR_RANK_AAA = 700

    IIDX_CLEAR_STATUS_NO_PLAY = 50
    IIDX_CLEAR_STATUS_FAILED = 100
    IIDX_CLEAR_STATUS_ASSIST_CLEAR = 200
    IIDX_CLEAR_STATUS_EASY_CLEAR = 300
    IIDX_CLEAR_STATUS_CLEAR = 400
    IIDX_CLEAR_STATUS_HARD_CLEAR = 500
    IIDX_CLEAR_STATUS_EX_HARD_CLEAR = 600
    IIDX_CLEAR_STATUS_FULL_COMBO = 700
    IIDX_DAN_RANK_7_KYU = 100
    IIDX_DAN_RANK_6_KYU = 200
    IIDX_DAN_RANK_5_KYU = 300
    IIDX_DAN_RANK_4_KYU = 400
    IIDX_DAN_RANK_3_KYU = 500
    IIDX_DAN_RANK_2_KYU = 600
    IIDX_DAN_RANK_1_KYU = 700
    IIDX_DAN_RANK_1_DAN = 800
    IIDX_DAN_RANK_2_DAN = 900
    IIDX_DAN_RANK_3_DAN = 1000
    IIDX_DAN_RANK_4_DAN = 1100
    IIDX_DAN_RANK_5_DAN = 1200
    IIDX_DAN_RANK_6_DAN = 1300
    IIDX_DAN_RANK_7_DAN = 1400
    IIDX_DAN_RANK_8_DAN = 1500
    IIDX_DAN_RANK_9_DAN = 1600
    IIDX_DAN_RANK_10_DAN = 1700
    IIDX_DAN_RANK_CHUDEN = 1800
    IIDX_DAN_RANK_KAIDEN = 1900

    JUBEAT_PLAY_MEDAL_FAILED = 100
    JUBEAT_PLAY_MEDAL_CLEARED = 200
    JUBEAT_PLAY_MEDAL_NEARLY_FULL_COMBO = 300
    JUBEAT_PLAY_MEDAL_FULL_COMBO = 400
    JUBEAT_PLAY_MEDAL_NEARLY_EXCELLENT = 500
    JUBEAT_PLAY_MEDAL_EXCELLENT = 600

    MUSECA_GRADE_DEATH = 100        # 没
    MUSECA_GRADE_POOR = 200         # 拙
    MUSECA_GRADE_MEDIOCRE = 300     # 凡
    MUSECA_GRADE_GOOD = 400         # 佳
    MUSECA_GRADE_GREAT = 500        # 良
    MUSECA_GRADE_EXCELLENT = 600    # 優
    MUSECA_GRADE_SUPERB = 700       # 秀
    MUSECA_GRADE_MASTERPIECE = 800  # 傑
    MUSECA_GRADE_PERFECT = 900      # 傑
    MUSECA_CLEAR_TYPE_FAILED = 100
    MUSECA_CLEAR_TYPE_CLEARED = 200
    MUSECA_CLEAR_TYPE_FULL_COMBO = 300

    POPN_MUSIC_PLAY_MEDAL_CIRCLE_FAILED = 100
    POPN_MUSIC_PLAY_MEDAL_DIAMOND_FAILED = 200
    POPN_MUSIC_PLAY_MEDAL_STAR_FAILED = 300
    POPN_MUSIC_PLAY_MEDAL_EASY_CLEAR = 400
    POPN_MUSIC_PLAY_MEDAL_CIRCLE_CLEARED = 500
    POPN_MUSIC_PLAY_MEDAL_DIAMOND_CLEARED = 600
    POPN_MUSIC_PLAY_MEDAL_STAR_CLEARED = 700
    POPN_MUSIC_PLAY_MEDAL_CIRCLE_FULL_COMBO = 800
    POPN_MUSIC_PLAY_MEDAL_DIAMOND_FULL_COMBO = 900
    POPN_MUSIC_PLAY_MEDAL_STAR_FULL_COMBO = 1000
    POPN_MUSIC_PLAY_MEDAL_PERFECT = 1100

    REFLEC_BEAT_CLEAR_TYPE_NO_PLAY = 100
    REFLEC_BEAT_CLEAR_TYPE_FAILED = 200
    REFLEC_BEAT_CLEAR_TYPE_CLEARED = 300
    REFLEC_BEAT_CLEAR_TYPE_HARD_CLEARED = 400
    REFLEC_BEAT_CLEAR_TYPE_S_HARD_CLEARED = 500
    REFLEC_BEAT_COMBO_TYPE_NONE = 100
    REFLEC_BEAT_COMBO_TYPE_ALMOST_COMBO = 200
    REFLEC_BEAT_COMBO_TYPE_FULL_COMBO = 300
    REFLEC_BEAT_COMBO_TYPE_FULL_COMBO_ALL_JUST = 400

    SDVX_CLEAR_TYPE_NO_PLAY = 50
    SDVX_CLEAR_TYPE_FAILED = 100
    SDVX_CLEAR_TYPE_CLEAR = 200
    SDVX_CLEAR_TYPE_HARD_CLEAR = 300
    SDVX_CLEAR_TYPE_ULTIMATE_CHAIN = 400
    SDVX_CLEAR_TYPE_PERFECT_ULTIMATE_CHAIN = 500
    SDVX_GRADE_NO_PLAY = 100
    SDVX_GRADE_D = 200
    SDVX_GRADE_C = 300
    SDVX_GRADE_B = 400
    SDVX_GRADE_A = 500
    SDVX_GRADE_A_PLUS = 550
    SDVX_GRADE_AA = 600
    SDVX_GRADE_AA_PLUS = 650
    SDVX_GRADE_AAA = 700
    SDVX_GRADE_AAA_PLUS = 800
    SDVX_GRADE_S = 900
