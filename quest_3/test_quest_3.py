import unittest
from quest_3 import find_symmetric_difference


class TestFindSymmetricDifference(unittest.TestCase):
    def test_find_symmetric_difference(self):
        """Проверка расчёта симметрической разности."""
        self.assertEqual(find_symmetric_difference("1 2 3 4 0 3 4 5 6 0"), "1 2 5 6")
        self.assertEqual(find_symmetric_difference("11 1 2 3 4 5 0 1 7 5 8 0"), "2 3 4 7 8 11")
        self.assertEqual(find_symmetric_difference("1 2 6 8 7 3 0 4 1 6 2 3 9"), "4 7 8 9")
        self.assertEqual(find_symmetric_difference("1 0 3"), "1 3")
        self.assertEqual(find_symmetric_difference("1 2 3 0 1 2 3"), "0")
        self.assertEqual(find_symmetric_difference("0 1"), "1")
        self.assertEqual(find_symmetric_difference("0"), "0")
        self.assertEqual(find_symmetric_difference("3 5 6 7 8 9 11 13 16 17 19 20 23 24 26 28 29 30 31 32 33 34 36 37 42 43 44 45 46 47 48 49 50 51 52 55"
                                                   "56 61 62 63 66 67 68 69 70 72 74 77 78 80 81 82 85 86 89 91 93 95 96 97 98 99 103 104 105 106 107 108 109"
                                                   "110 111 114 115 116 117 120 122 123 124 125 127 128 129 130 131 138 140 141 142 143 144 145 146 148 149 150"
                                                   "151 152 153 154 155 156 157 160 161 163 164 165 166 168 169 170 175 176 177 178 180 181 184 185 186 187 188"
                                                   "189 192 193 194 195 196 199 200 202 203 205 206 207 209 210 211 212 213 214 215 217 218 219 220 221 225 226 228"
                                                   "229 230 232 233 234 235 236 238 240 241 242 243 244 245 246 247 248 250 253 254 255 256 257 259 262 263 264 268 269"
                                                   "270 271 273 274 275 276 279 281 282 284 287 288 289 294 295 296 297 298 299 300 0 1 2 3 5 6 7 8 10 11 14 15 16 18 19"
                                                   "20 21 24 25 26 27 28 29 31 33 34 35 36 37 38 39 41 42 44 45 46 47 48 49 52 53 55 56 57 58 59 60 62 65 67 68 70 71 72"
                                                   "73 74 76 77 79 80 82 83 84 86 87 88 89 90 91 96 97 98 99 100 102 103 105 106 107 109 110 111 113 114 115 116 117 118"
                                                   "119 121 123 124 125 128 129 130 131 133 134 138 142 143 144 145 146 147 148 151 152 153 159 160 161 162 163 164 166 167"
                                                   "168 169 170 172 174 175 176 177 179 180 181 182 183 184 185 186 187 188 192 193 195 197 199 200 201 202 203 204 205 206"
                                                   "207 209 210 211 212 213 220 221 224 229 231 232 233 237 238 243 244 246 248 251 252 253 255 256 257 258 259 260 262 265 266"
                                                   "268 271 272 274 275 276 277 278 281 283 285 286 288 289 290 291 292 293 294 298 299 300"), "2 5 6 7 8 9 11 13 16 17 19 23 24 26 28 29")

