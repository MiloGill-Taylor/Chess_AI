from bitarray import bitarray

material_dictionary={"white pawn":1, "white knight":2,"white queen":3, "white bishop":4,"white rook":5,"white king":6,"black pawn":7,"black knight":8,"black queen":9,"black bishop":10, "black rook":11,"black king":12}

class bitboard(bitarray):
    def __init__(self,piece_id):
        super().__init__()
        for i in range(64):
            self.append(0)
        self.piece_id=piece_id
        #some code here setting up the bitboard for the beginning of the game based upon the piece given
    def piece_name(self):
        return material_dictionary[self.piece_id]


class gamestate():
    def __init__(self):
        self.bitboards=[]
        for i in range(12):
            if i==0:
                key="white pawn"
            elif i==1:
                key="white knight"
            elif i==2:
                key="white queen"
            elif i==3:
                key="white bishop"
            elif i==4:
                key="white rook"
            elif i==5:
                key="white king"
            elif i==6:
                key="black pawn"
            elif i==7:
                key="black knight"
            elif i==8:
                key="black queen"
            elif i==9:
                key="black bishop"
            elif i==10:
                key="black rook"
            else:
                key="black king"
            new_bitboard=bitboard(material_dictionary[key])
            self.bitboards.append(new_bitboard)          


state=gamestate()

print(state.bitboards[0].piece_name)



