def calc_bowlingScores(game1, game2, game3, handicap):
    avgscore = (game1 + game2 + game3) / 3
    avg_with_handicap = avgscore + handicap
    return (avgscore, avg_with_handicap)
def main():
    lastname = input("Enter the bowler's last name: ")
    game1 = float(input("Enter the first game score: "))
    game2 = float(input("Enter the second game score: "))
    game3 = float(input("Enter the third game score: "))
    handicap = float(input("Enter the handicap: "))
    avgscore, avg_with_handicap = calc_bowlingScores(game1, game2, game3, handicap)
    print(f"Bowler's Last Name: {lastname}")
    print(f"Average Score: {avgscore:.2f}")
    print(f"Average Score with Handicap: {avg_with_handicap:.2f}")
main()