from atlas.game.Cube import CubeColour
from atlas.game.flag import FlagRepository, Flag

FLAGS = {
    "1": {
        "pattern": [
            ["", "", ""],
            ["BLACK", "RED", "GREEN"],
            ["", "", ""]
        ],
        "_raw_string": "\ufeff1\tAfghanistan\t\n",
        "_file_name": "Flag_Afghanistan.gif"
    },
    "2": {
        "pattern": [
            ["GREEN", "RED", "RED"],
            ["BLACK", "GREEN", "GREEN"],
            ["GREEN", "BLUE", "BLUE"]
        ],
        "_raw_string": "2\tAfrique du Sud\t\n",
        "_file_name": "Flag_AfriqueSud.gif"
    },
    "3": {
        "pattern": [
            ["", "", ""],
            ["", "BLACK", ""],
            ["", "", ""]
        ],
        "_raw_string": "3\tAlbanie\t\n",
        "_file_name": "Flag_Albanie.gif"
    },
    "4": {
        "pattern": [
            ["", "", ""],
            ["GREEN", "RED", "WHITE"],
            ["", "", ""]
        ],
        "_raw_string": "4\tAlg\u00e9rie\t\n",
        "_file_name": "Flag_Algerie.gif"
    },
    "5": {
        "pattern": [
            ["", "BLACK", ""],
            ["", "RED", ""],
            ["", "YELLOW", ""]
        ],
        "_raw_string": "5\tAllemagne\t\n",
        "_file_name": "Flag_Allemagne.gif"
    },
    "6": {
        "pattern": [
            ["", "", ""],
            ["BLUE", "YELLOW", "RED"],
            ["", "", ""]
        ],
        "_raw_string": "6\tAndorre\t\n",
        "_file_name": "Flag_Andorre.gif"
    },
    "7": {
        "pattern": [
            ["", "RED", ""],
            ["", "BLACK", ""],
            ["", "", ""]
        ],
        "_raw_string": "7\tAngola\t\n",
        "_file_name": "Flag_Angola.gif"
    },
    "8": {
        "pattern": [
            ["", "", ""],
            ["BLACK", "BLACK", "BLACK"],
            ["RED", "BLUE", "RED"]
        ],
        "_raw_string": "8\tAntigua-et-Barbuda\t\n",
        "_file_name": "Flag_Antigua-Barbuda.gif"
    },
    "9": {
        "pattern": [
            ["", "", ""],
            ["GREEN", "WHITE", "GREEN"],
            ["", "", ""]
        ],
        "_raw_string": "9\tArabie Saoudite\t\n",
        "_file_name": "Flag_Arabie-Saoudite.gif"
    },
    "10": {
        "pattern": [
            ["", "BLUE", ""],
            ["", "WHITE", ""],
            ["", "BLUE", ""]
        ],
        "_raw_string": "10\tArgentine\t\n",
        "_file_name": "Flag_Argentine.gif"
    },
    "11": {
        "pattern": [
            ["", "RED", ""],
            ["", "BLUE", ""],
            ["", "YELLOW", ""]
        ],
        "_raw_string": "11\tArm\u00e9nie\t\n",
        "_file_name": "Flag_Armenie.gif"
    },
    "12": {
        "pattern": [
            ["RED", "BLUE", ""],
            ["BLUE", "BLUE", ""],
            ["", "", ""]
        ],
        "_raw_string": "12\tAustralie\t\n",
        "_file_name": "Flag_Australie.gif"
    },
    "13": {
        "pattern": [
            ["", "RED", ""],
            ["", "WHITE", ""],
            ["", "RED", ""]
        ],
        "_raw_string": "13\tAutriche\t\n",
        "_file_name": "Flag_Autriche.gif"
    },
    "14": {
        "pattern": [
            ["", "BLUE", ""],
            ["", "RED", ""],
            ["", "GREEN", ""]
        ],
        "_raw_string": "14\tAzerba\u00efdjan\t\n",
        "_file_name": "Flag_Azerbaidjan.gif"
    },
    "15": {
        "pattern": [
            ["BLUE", "BLUE", ""],
            ["BLACK", "YELLOW", ""],
            ["BLUE", "BLUE", ""]
        ],
        "_raw_string": "15\tBahamas\t\n",
        "_file_name": "Flag_Bahamas.gif"
    },
    "16": {
        "pattern": [
            ["", "", ""],
            ["WHITE", "RED", "RED"],
            ["", "", ""]
        ],
        "_raw_string": "16\tBahre\u00efn\t\n",
        "_file_name": "Flag_Bahrein.gif"
    },
    "17": {
        "pattern": [
            ["", "", ""],
            ["WHITE", "WHITE", "WHITE"],
            ["GREEN", "RED", "GREEN"]
        ],
        "_raw_string": "17\tBangladesh\t\n",
        "_file_name": "Flag_Bangladesh.gif"
    },
    "18": {
        "pattern": [
            ["", "", ""],
            ["BLUE", "YELLOW", "BLUE"],
            ["", "", ""]
        ],
        "_raw_string": "18\tBarbade\t\n",
        "_file_name": "Flag_Barbade.gif"
    },
    "19": {
        "pattern": [
            ["RED", "RED", ""],
            ["RED", "RED", ""],
            ["GREEN", "GREEN", ""]
        ],
        "_raw_string": "19\tBelarusse\t\n",
        "_file_name": "Flag_Belarusse.gif"
    },
    "20": {
        "pattern": [
            ["", "", ""],
            ["BLACK", "YELLOW", "RED"],
            ["", "", ""]
        ],
        "_raw_string": "20\tBelgique\t\n",
        "_file_name": "Flag_Belgique.gif"
    },
    "21": {
        "pattern": [
            ["", "", ""],
            ["BLUE", "WHITE", "BLUE"],
            ["", "", ""]
        ],
        "_raw_string": "21\tBelize\t\n",
        "_file_name": "Flag_Belize.gif"
    },
    "22": {
        "pattern": [
            ["GREEN", "YELLOW", ""],
            ["GREEN", "RED", ""],
            ["", "", ""]
        ],
        "_raw_string": "22\tB\u00e9nin\t\n",
        "_file_name": "Flag_Benin.gif"
    },
    "23": {
        "pattern": [
            ["", "", ""],
            ["YELLOW", "YELLOW", "RED"],
            ["YELLOW", "RED", "RED"]
        ],
        "_raw_string": "23\tBhoutan\t\n",
        "_file_name": "Flag_Bhoutan.gif"
    },
    "24": {
        "pattern": [
            ["", "RED", ""],
            ["", "YELLOW", ""],
            ["", "GREEN", ""]
        ],
        "_raw_string": "24\tBolivie\t\n",
        "_file_name": "Flag_Bolivie.gif"
    },
    "25": {
        "pattern": [
            ["", "", ""],
            ["BLUE", "YELLOW", ""],
            ["BLUE", "BLUE", ""]
        ],
        "_raw_string": "25\tBosnie-Herz\u00e9govine\t\n",
        "_file_name": "Flag_Bosnie.gif"
    },
    "26": {
        "pattern": [
            ["", "BLUE", ""],
            ["", "BLACK", ""],
            ["", "BLUE", ""]
        ],
        "_raw_string": "26\tBotswana\t\n",
        "_file_name": "Flag_Botswana.gif"
    },
    "27": {
        "pattern": [
            ["GREEN", "YELLOW", "GREEN"],
            ["YELLOW", "BLUE", "YELLOW"],
            ["GREEN", "YELLOW", "GREEN"]
        ],
        "_raw_string": "27\tBr\u00e9sil\t\n",
        "_file_name": "Flag_Bresil.gif"
    },
    "28": {
        "pattern": [
            ["", "YELLOW", ""],
            ["", "BLACK", ""],
            ["", "YELLOW", ""]
        ],
        "_raw_string": "28\tBrunei\t\n",
        "_file_name": "Flag_Brunei.gif"
    },
    "29": {
        "pattern": [
            ["", "WHITE", ""],
            ["", "GREEN", ""],
            ["", "RED", ""]
        ],
        "_raw_string": "29\tBulgarie\t\n",
        "_file_name": "Flag_Bulgarie.gif"
    },
    "30": {
        "pattern": [
            ["", "", ""],
            ["", "RED", ""],
            ["", "GREEN", ""]
        ],
        "_raw_string": "30\tBurkina Faso\t\n",
        "_file_name": "Flag_Burkina.gif"
    },
    "31": {
        "pattern": [
            ["WHITE", "RED", "WHITE"],
            ["GREEN", "RED", "GREEN"],
            ["WHITE", "RED", "WHITE"]
        ],
        "_raw_string": "31\tBurundi\t\n",
        "_file_name": "Flag_Burundi.gif"
    },
    "32": {
        "pattern": [
            ["", "BLUE", ""],
            ["", "RED", ""],
            ["", "BLUE", ""]
        ],
        "_raw_string": "32\tCambodge\t\n",
        "_file_name": "Flag_Cambodge.gif"
    },
    "33": {
        "pattern": [
            ["", "", ""],
            ["", "", ""],
            ["GREEN", "RED", "YELLOW"]
        ],
        "_raw_string": "33\tCameroun\t\n",
        "_file_name": "Flag_Cameroun.gif"
    },
    "34": {
        "pattern": [
            ["", "", ""],
            ["RED", "WHITE", "RED"],
            ["", "", ""]
        ],
        "_raw_string": "34\tCanada\t\n",
        "_file_name": "Flag_Canada.gif"
    },
    "35": {
        "pattern": [
            ["", "", ""],
            ["BLUE", "BLUE", "BLUE"],
            ["RED", "YELLOW", "RED"]
        ],
        "_raw_string": "35\tCap-Vert\t\n",
        "_file_name": "Flag_Cap-Vert.gif"
    },
    "36": {
        "pattern": [
            ["BLUE", "RED", "BLUE"],
            ["WHITE", "RED", "GREEN"],
            ["YELLOW", "RED", "YELLOW"]
        ],
        "_raw_string": "36\tCentrafrique\t\n",
        "_file_name": "Flag_Centrafique.gif"
    },
    "37": {
        "pattern": [
            ["", "", ""],
            ["BLUE", "WHITE", ""],
            ["RED", "RED", ""]
        ],
        "_raw_string": "37\tChili\t\n",
        "_file_name": "Flag_Chili.gif"
    },
    "38": {
        "pattern": [
            ["", "", ""],
            ["YELLOW", "RED", ""],
            ["RED", "RED", ""]
        ],
        "_raw_string": "38\tChine\t\n",
        "_file_name": "Flag_Chine.gif"
    },
    "39": {
        "pattern": [
            ["", "", ""],
            ["", "YELLOW", ""],
            ["", "", ""]
        ],
        "_raw_string": "39\tChypre\t\n",
        "_file_name": "Flag_Chypre.gif"
    },
    "40": {
        "pattern": [
            ["", "YELLOW", ""],
            ["", "BLUE", ""],
            ["", "RED", ""]
        ],
        "_raw_string": "40\tColombie\t\n",
        "_file_name": "Flag_Colombie.gif"
    },
    "41": {
        "pattern": [
            ["GREEN", "YELLOW", "YELLOW"],
            ["GREEN", "GREEN", "RED"],
            ["GREEN", "BLUE", "BLUE"]
        ],
        "_raw_string": "41\tComores\t\n",
        "_file_name": "Flag_Comores.gif"
    },
    "42": {
        "pattern": [
            ["GREEN", "GREEN", "YELLOW"],
            ["GREEN", "YELLOW", "RED"],
            ["YELLOW", "RED", "RED"]
        ],
        "_raw_string": "42\tCongo\t\n",
        "_file_name": "Flag_Congo.gif"
    },
    "43": {
        "pattern": [
            ["", "", ""],
            ["YELLOW", "BLUE", "RED"],
            ["BLUE", "RED", "BLUE"]
        ],
        "_raw_string": "43\tCongo, R\u00e9publique d\u00e9mocratique\t\n",
        "_file_name": "Flag_CongoRD.gif"
    },
    "44": {
        "pattern": [
            ["BLUE", "BLUE", ""],
            ["YELLOW", "RED", ""],
            ["BLUE", "BLUE", ""]
        ],
        "_raw_string": "44\tCor\u00e9e du Nord\t\n",
        "_file_name": "Flag_CoreeN.gif"
    },
    "45": {
        "pattern": [
            ["BLACK", "WHITE", "BLACK"],
            ["WHITE", "RED", "WHITE"],
            ["BLACK", "WHITE", "BLACK"]
        ],
        "_raw_string": "45\tCor\u00e9e du Sud\t\n",
        "_file_name": "Flag_CoreeS.gif"
    },
    "46": {
        "pattern": [
            ["", "BLUE", ""],
            ["", "RED", ""],
            ["", "BLUE", ""]
        ],
        "_raw_string": "46\tCosta Rica\t\n",
        "_file_name": "Flag_CostaRica.gif"
    },
    "47": {
        "pattern": [
            ["", "", ""],
            ["", "", ""],
            ["RED", "WHITE", "GREEN"]
        ],
        "_raw_string": "47\tC\u00f4te d'Ivoire\t\n",
        "_file_name": "Flag_CoteIvoire.gif"
    },
    "48": {
        "pattern": [
            ["RED", "RED", "RED"],
            ["WHITE", "RED", "WHITE"],
            ["BLUE", "BLUE", "BLUE"]
        ],
        "_raw_string": "48\tCroatie\t\n",
        "_file_name": "Flag_Croatie.gif"
    },
    "49": {
        "pattern": [
            ["BLUE", "BLUE", ""],
            ["RED", "WHITE", ""],
            ["BLUE", "BLUE", ""]
        ],
        "_raw_string": "49\tCuba\t\n",
        "_file_name": "Flag_Cuba.gif"
    },
    "50": {
        "pattern": [
            ["RED", "WHITE", "RED"],
            ["WHITE", "YELLOW", "WHITE"],
            ["RED", "WHITE", "RED"]
        ],
        "_raw_string": "50\tDanemark\t\n",
        "_file_name": "Flag_Danemark.gif"
    },
    "51": {
        "pattern": [
            ["", "", ""],
            ["WHITE", "BLUE", "BLUE"],
            ["WHITE", "GREEN", "GREEN"]
        ],
        "_raw_string": "51\tDjibouti\t\n",
        "_file_name": "Flag_Djibouti.gif"
    },
    "52": {
        "pattern": [
            ["GREEN", "BLACK", "GREEN"],
            ["YELLOW", "RED", "YELLOW"],
            ["GREEN", "WHITE", "GREEN"]
        ],
        "_raw_string": "52\tDominique\t\n",
        "_file_name": "Flag_Dominique.gif"
    },
    "53": {
        "pattern": [
            ["", "RED", ""],
            ["", "WHITE", ""],
            ["", "BLACK", ""]
        ],
        "_raw_string": "53\tEgypte\t\n",
        "_file_name": "Flag_Egypte.gif"
    },
    "54": {
        "pattern": [
            ["", "BLUE", ""],
            ["", "WHITE", ""],
            ["", "BLUE", ""]
        ],
        "_raw_string": "54\tEl Salvador\t\n",
        "_file_name": "Flag_ElSalvador.gif"
    },
    "55": {
        "pattern": [
            ["RED", "GREEN", ""],
            ["RED", "WHITE", ""],
            ["RED", "BLACK", ""]
        ],
        "_raw_string": "55\tEmirats Arabes Unis\t\n",
        "_file_name": "Flag_EmiratsArabesUnis.gif"
    },
    "56": {
        "pattern": [
            ["", "YELLOW", ""],
            ["", "BLUE", ""],
            ["", "RED", ""]
        ],
        "_raw_string": "56\tEquateur\t\n",
        "_file_name": "Flag_Equateur.gif"
    },
    "57": {
        "pattern": [
            ["RED", "GREEN", ""],
            ["RED", "RED", ""],
            ["RED", "BLUE", ""]
        ],
        "_raw_string": "57\tErythr\u00e9e\t\n",
        "_file_name": "Flag_Erythree.gif"
    },
    "58": {
        "pattern": [
            ["", "RED", ""],
            ["", "YELLOW", ""],
            ["", "RED", ""]
        ],
        "_raw_string": "58\tEspagne\t\n",
        "_file_name": "Flag_Espagne.gif"
    },
    "59": {
        "pattern": [
            ["", "BLUE", ""],
            ["", "BLACK", ""],
            ["", "WHITE", ""]
        ],
        "_raw_string": "59\tEstonie\t\n",
        "_file_name": "Flag_Estonie.gif"
    },
    "60": {
        "pattern": [
            ["BLUE", "RED", ""],
            ["WHITE", "WHITE", ""],
            ["RED", "RED", ""]
        ],
        "_raw_string": "60\tEtats-Unis\t\n",
        "_file_name": "Flag_EtatsUnis.gif"
    },
    "61": {
        "pattern": [
            ["", "GREEN", ""],
            ["", "YELLOW", ""],
            ["", "RED", ""]
        ],
        "_raw_string": "61\tEthiopie\t\n",
        "_file_name": "Flag_Ethiopie.gif"
    },
    "62": {
        "pattern": [
            ["WHITE", "BLUE", "WHITE"],
            ["BLUE", "BLACK", "BLUE"],
            ["WHITE", "BLUE", "WHITE"]
        ],
        "_raw_string": "62\tFinlande\t\n",
        "_file_name": "Flag_Finlande.gif"
    },
    "63": {
        "pattern": [
            ["", "", ""],
            ["", "", ""],
            ["BLUE", "WHITE", "RED"]
        ],
        "_raw_string": "63\tFrance\t\n",
        "_file_name": "Flag_France.gif"
    },
    "64": {
        "pattern": [
            ["", "GREEN", ""],
            ["", "YELLOW", ""],
            ["", "BLUE", ""]
        ],
        "_raw_string": "64\tGabon\t\n",
        "_file_name": "Flag_Gabon.gif"
    },
    "65": {
        "pattern": [
            ["", "RED", ""],
            ["", "BLUE", ""],
            ["", "GREEN", ""]
        ],
        "_raw_string": "65\tGambie\t\n",
        "_file_name": "Flag_Gambie.gif"
    },
    "66": {
        "pattern": [
            ["WHITE", "RED", "WHITE"],
            ["RED", "YELLOW", "RED"],
            ["WHITE", "RED", "WHITE"]
        ],
        "_raw_string": "66\tG\u00e9orgie\t\n",
        "_file_name": "Flag_Georgie.gif"
    },
    "67": {
        "pattern": [
            ["", "RED", ""],
            ["", "YELLOW", ""],
            ["", "GREEN", ""]
        ],
        "_raw_string": "67\tGhana\t\n",
        "_file_name": "Flag_Ghana.gif"
    },
    "68": {
        "pattern": [
            ["", "BLUE", ""],
            ["", "WHITE", ""],
            ["", "BLUE", ""]
        ],
        "_raw_string": "68\tGr\u00e8ce\t\n",
        "_file_name": "Flag_Grece.gif"
    },
    "69": {
        "pattern": [
            ["YELLOW", "YELLOW", "GREEN"],
            ["GREEN", "RED", "GREEN"],
            ["GREEN", "YELLOW", "YELLOW"]
        ],
        "_raw_string": "69\tGrenade\t\n",
        "_file_name": "Flag_Grenade.gif"
    },
    "70": {
        "pattern": [
            ["", "", ""],
            ["", "", ""],
            ["BLUE", "WHITE", "BLUE"]
        ],
        "_raw_string": "70\tGuatemala\t\n",
        "_file_name": "Flag_Guatemala.gif"
    },
    "71": {
        "pattern": [
            ["", "", ""],
            ["", "", ""],
            ["RED", "YELLOW", "GREEN"]
        ],
        "_raw_string": "71\tGuin\u00e9e\t\n",
        "_file_name": "Flag_Guinee.gif"
    },
    "73": {
        "pattern": [
            ["", "", ""],
            ["RED", "YELLOW", ""],
            ["RED", "GREEN", ""]
        ],
        "_raw_string": "73\tGuin\u00e9e-Bissau\t\n",
        "_file_name": "Flag_GuineeBissau.gif"
    },
    "72": {
        "pattern": [
            ["GREEN", "GREEN", ""],
            ["BLUE", "WHITE", ""],
            ["RED", "RED", ""]
        ],
        "_raw_string": "72\tGuin\u00e9e \u00e9quatoriale\t\n",
        "_file_name": "Flag_GuineeEquatoriale.gif"
    },
    "74": {
        "pattern": [
            ["GREEN", "GREEN", ""],
            ["RED", "YELLOW", ""],
            ["GREEN", "GREEN", ""]
        ],
        "_raw_string": "74\tGuyana\t\n",
        "_file_name": "Flag_Guyana.gif"
    },
    "75": {
        "pattern": [
            ["", "", ""],
            ["", "BLUE", ""],
            ["", "RED", ""]
        ],
        "_raw_string": "75\tHa\u00efti\t\n",
        "_file_name": "Flag_Haiti.gif"
    },
    "76": {
        "pattern": [
            ["", "BLUE", ""],
            ["", "WHITE", ""],
            ["", "BLUE", ""]
        ],
        "_raw_string": "76\tHonduras\t\n",
        "_file_name": "Flag_Honduras.gif"
    },
    "77": {
        "pattern": [
            ["", "RED", ""],
            ["", "WHITE", ""],
            ["", "GREEN", ""]
        ],
        "_raw_string": "77\tHongrie\t\n",
        "_file_name": "Flag_Hongrie.gif"
    },
    "78": {
        "pattern": [
            ["", "", ""],
            ["RED", "BLUE", ""],
            ["BLUE", "WHITE", ""]
        ],
        "_raw_string": "78\tIle Cook\t\n",
        "_file_name": "Flag_IlesCook.gif"
    },
    "79": {
        "pattern": [
            ["", "", ""],
            ["RED", "BLUE", ""],
            ["BLUE", "BLUE", ""]
        ],
        "_raw_string": "79\tIles Fidji\t\n",
        "_file_name": "Flag_IlesFidji.gif"
    },
    "80": {
        "pattern": [
            ["BLUE", "BLUE", "RED"],
            ["WHITE", "RED", "YELLOW"],
            ["RED", "BLUE", "BLUE"]
        ],
        "_raw_string": "80\tIles Marshall\t\n",
        "_file_name": "Flag_IlesMarshall.gif"
    },
    "81": {
        "pattern": [
            ["WHITE", "BLUE", "YELLOW"],
            ["BLUE", "YELLOW", "GREEN"],
            ["YELLOW", "GREEN", "GREEN"]
        ],
        "_raw_string": "81\tIles Salomon\t\n",
        "_file_name": "Flag_IlesSalomon.gif"
    },
    "82": {
        "pattern": [
            ["", "YELLOW", ""],
            ["", "WHITE", ""],
            ["", "GREEN", ""]
        ],
        "_raw_string": "82\tInde\t\n",
        "_file_name": "Flag_Inde.gif"
    },
    "83": {
        "pattern": [
            ["", "", ""],
            ["", "RED", ""],
            ["", "WHITE", ""]
        ],
        "_raw_string": "83\tIndon\u00e9sie\t\n",
        "_file_name": "Flag_Indonesie.gif"
    },
    "84": {
        "pattern": [
            ["", "RED", ""],
            ["", "WHITE", ""],
            ["", "BLACK", ""]
        ],
        "_raw_string": "84\tIrak\t\n",
        "_file_name": "Flag_Irak.gif"
    },
    "85": {
        "pattern": [
            ["", "GREEN", ""],
            ["", "WHITE", ""],
            ["", "RED", ""]
        ],
        "_raw_string": "85\tIran\t\n",
        "_file_name": "Flag_Iran.gif"
    },
    "86": {
        "pattern": [
            ["", "", ""],
            ["", "", ""],
            ["GREEN", "WHITE", "YELLOW"]
        ],
        "_raw_string": "86\tIrlande\t\n",
        "_file_name": "Flag_Irlande.gif"
    },
    "87": {
        "pattern": [
            ["BLUE", "RED", "BLUE"],
            ["RED", "YELLOW", "RED"],
            ["BLUE", "RED", "BLUE"]
        ],
        "_raw_string": "87\tIslande\t\n",
        "_file_name": "Flag_Islande.gif"
    },
    "88": {
        "pattern": [
            ["BLUE", "BLUE", ""],
            ["WHITE", "WHITE", ""],
            ["BLUE", "BLUE", ""]
        ],
        "_raw_string": "88\tIsra\u00ebl\t\n",
        "_file_name": "Flag_Israel.gif"
    },
    "89": {
        "pattern": [
            ["", "", ""],
            ["", "", ""],
            ["GREEN", "WHITE", "RED"]
        ],
        "_raw_string": "89\tItalie\t\n",
        "_file_name": "Flag_Italie.gif"
    },
    "90": {
        "pattern": [
            ["YELLOW", "GREEN", "YELLOW"],
            ["BLACK", "WHITE", "BLACK"],
            ["YELLOW", "GREEN", "YELLOW"]
        ],
        "_raw_string": "90\tJama\u00efque\t\n",
        "_file_name": "Flag_Jamaique.gif"
    },
    "91": {
        "pattern": [
            ["", "", ""],
            ["", "RED", ""],
            ["", "", ""]
        ],
        "_raw_string": "91\tJapon\t\n",
        "_file_name": "Flag_Japon.gif"
    },
    "92": {
        "pattern": [
            ["BLACK", "BLACK", "BLACK"],
            ["RED", "WHITE", "WHITE"],
            ["GREEN", "GREEN", "GREEN"]
        ],
        "_raw_string": "92\tJordanie\t\n",
        "_file_name": "Flag_Jordanie.gif"
    },
    "93": {
        "pattern": [
            ["", "", ""],
            ["", "", ""],
            ["BLUE", "YELLOW", "BLUE"]
        ],
        "_raw_string": "93\tKazakhstan\t\n",
        "_file_name": "Flag_Kazakhstan.gif"
    },
    "94": {
        "pattern": [
            ["", "BLACK", ""],
            ["", "RED", ""],
            ["", "GREEN", ""]
        ],
        "_raw_string": "94\tKenya\t\n",
        "_file_name": "Flag_Kenya.gif"
    },
    "95": {
        "pattern": [
            ["", "", ""],
            ["", "YELLOW", ""],
            ["", "", ""]
        ],
        "_raw_string": "95\tKirghizistan\t\n",
        "_file_name": "Flag_Kirghizistan.gif"
    },
    "96": {
        "pattern": [
            ["", "", ""],
            ["RED", "YELLOW", "RED"],
            ["BLUE", "BLUE", "BLUE"]
        ],
        "_raw_string": "96\tKiribati\t\n",
        "_file_name": "Flag_Kiribati.gif"
    },
    "97": {
        "pattern": [
            ["GREEN", "GREEN", ""],
            ["BLACK", "WHITE", ""],
            ["RED", "RED", ""]
        ],
        "_raw_string": "97\tKowe\u00eft\t\n",
        "_file_name": "Flag_Koweit.gif"
    },
    "98": {
        "pattern": [
            ["RED", "RED", ""],
            ["BLUE", "WHITE", ""],
            ["RED", "RED", ""]
        ],
        "_raw_string": "98\tLaos\t\n",
        "_file_name": "Flag_Laos.gif"
    },
    "99": {
        "pattern": [
            ["", "BLUE", ""],
            ["", "WHITE", ""],
            ["", "GREEN", ""]
        ],
        "_raw_string": "99\tLesotho\t\n",
        "_file_name": "Flag_Lesotho.gif"
    },
    "100": {
        "pattern": [
            ["", "RED", ""],
            ["", "WHITE", ""],
            ["", "RED", ""]
        ],
        "_raw_string": "100\tLettonie\t\n",
        "_file_name": "Flag_Lettonie.gif"
    },
    "101": {
        "pattern": [
            ["RED", "RED", ""],
            ["WHITE", "GREEN", ""],
            ["RED", "RED", ""]
        ],
        "_raw_string": "101\tLiban\t\n",
        "_file_name": "Flag_Liban.gif"
    },
    "102": {
        "pattern": [
            ["BLUE", "RED", ""],
            ["WHITE", "WHITE", ""],
            ["RED", "RED", ""]
        ],
        "_raw_string": "102\tLiberia\t\n",
        "_file_name": "Flag_Liberia.gif"
    },
    "103": {
        "pattern": [
            ["", "BLACK", ""],
            ["", "RED", ""],
            ["", "GREEN", ""]
        ],
        "_raw_string": "103\tLibye\t\n",
        "_file_name": "Flag_Libye.gif"
    },
    "104": {
        "pattern": [
            ["", "", ""],
            ["", "RED", ""],
            ["", "BLUE", ""]
        ],
        "_raw_string": "104\tLiechtenstein\t\n",
        "_file_name": "Flag_Liechtenstein.gif"
    },
    "105": {
        "pattern": [
            ["", "YELLOW", ""],
            ["", "GREEN", ""],
            ["", "RED", ""]
        ],
        "_raw_string": "105\tLituanie\t\n",
        "_file_name": "Flag_Lituanie.gif"
    },
    "106": {
        "pattern": [
            ["", "RED", ""],
            ["", "WHITE", ""],
            ["", "BLUE", ""]
        ],
        "_raw_string": "106\tLuxembourg\t\n",
        "_file_name": "Flag_Luxembourg.gif"
    },
    "107": {
        "pattern": [
            ["YELLOW", "RED", "YELLOW"],
            ["RED", "WHITE", "RED"],
            ["YELLOW", "RED", "YELLOW"]
        ],
        "_raw_string": "107\tMac\u00e9doine\t\n",
        "_file_name": "Flag_Macedoine.gif"
    },
    "108": {
        "pattern": [
            ["", "", ""],
            ["WHITE", "RED", ""],
            ["WHITE", "GREEN", ""]
        ],
        "_raw_string": "108\tMadagascar\t\n",
        "_file_name": "Flag_Madagascar.gif"
    },
    "109": {
        "pattern": [
            ["BLUE", "RED", ""],
            ["WHITE", "WHITE", ""],
            ["RED", "RED", ""]
        ],
        "_raw_string": "109\tMalaisie\t\n",
        "_file_name": "Flag_Malaisie.gif"
    },
    "110": {
        "pattern": [
            ["", "BLACK", ""],
            ["", "RED", ""],
            ["", "GREEN", ""]
        ],
        "_raw_string": "110\tMalawi\t\n",
        "_file_name": "Flag_Malawi.gif"
    },
    "111": {
        "pattern": [
            ["RED", "RED", ""],
            ["GREEN", "WHITE", ""],
            ["RED", "RED", ""]
        ],
        "_raw_string": "111\tMaldives\t\n",
        "_file_name": "Flag_Maldives.gif"
    },
    "112": {
        "pattern": [
            ["", "", ""],
            ["", "", ""],
            ["GREEN", "YELLOW", "RED"]
        ],
        "_raw_string": "112\tMali\t\n",
        "_file_name": "Flag_Mali.gif"
    },
    "113": {
        "pattern": [
            ["", "", ""],
            ["", "", ""],
            ["WHITE", "RED", ""]
        ],
        "_raw_string": "113\tMalte\t\n",
        "_file_name": "Flag_Malte.gif"
    },
    "114": {
        "pattern": [
            ["", "", ""],
            ["", "", ""],
            ["RED", "GREEN", "RED"]
        ],
        "_raw_string": "114\tMaroc\t\n",
        "_file_name": "Flag_Maroc.gif"
    },
    "115": {
        "pattern": [
            ["", "RED", ""],
            ["", "YELLOW", ""],
            ["", "GREEN", ""]
        ],
        "_raw_string": "115\tMaurice\t\n",
        "_file_name": "Flag_Maurice.gif"
    },
    "116": {
        "pattern": [
            ["", "GREEN", ""],
            ["", "YELLOW", ""],
            ["", "GREEN", ""]
        ],
        "_raw_string": "116\tMauritanie\t\n",
        "_file_name": "Flag_Mauritanie.gif"
    },
    "117": {
        "pattern": [
            ["", "", ""],
            ["", "", ""],
            ["GREEN", "WHITE", "RED"]
        ],
        "_raw_string": "117\tMexique\t\n",
        "_file_name": "Flag_Mexique.gif"
    },
    "118": {
        "pattern": [
            ["BLUE", "WHITE", "BLUE"],
            ["WHITE", "GREEN", "WHITE"],
            ["BLUE", "WHITE", "BLUE"]
        ],
        "_raw_string": "118\tMicron\u00e9sie\t\n",
        "_file_name": "Flag_Micronesie.gif"
    },
    "119": {
        "pattern": [
            ["", "", ""],
            ["", "", ""],
            ["BLUE", "YELLOW", "RED"]
        ],
        "_raw_string": "119\tMoldavie\t\n",
        "_file_name": "Flag_Moldova.gif"
    },
    "120": {
        "pattern": [
            ["", "", ""],
            ["", "RED", ""],
            ["", "WHITE", ""]
        ],
        "_raw_string": "120\tMonaco\t\n",
        "_file_name": "Flag_Monaco.gif"
    },
    "121": {
        "pattern": [
            ["", "", ""],
            ["", "", ""],
            ["RED", "BLUE", "RED"]
        ],
        "_raw_string": "121\tMongolie\t\n",
        "_file_name": "Flag_Mongolie.gif"
    },
    "122": {
        "pattern": [
            ["", "", ""],
            ["", "", ""],
            ["RED", "YELLOW", "RED"]
        ],
        "_raw_string": "122\tMont\u00e9n\u00e9gro\t\n",
        "_file_name": "Flag_Montenegro.gif"
    },
    "123": {
        "pattern": [
            ["RED", "GREEN", "GREEN"],
            ["RED", "RED", "BLUE"],
            ["RED", "YELLOW", "YELLOW"]
        ],
        "_raw_string": "123\tMozambique\t\n",
        "_file_name": "Flag_Mozambique.gif"
    },
    "124": {
        "pattern": [
            ["YELLOW", "YELLOW", "YELLOW"],
            ["GREEN", "WHITE", "GREEN"],
            ["RED", "RED", "RED"]
        ],
        "_raw_string": "124\tMyanmar\t\n",
        "_file_name": "Flag_Myanmar.gif"
    },
    "125": {
        "pattern": [
            ["YELLOW", "BLUE", "RED"],
            ["BLUE", "RED", "GREEN"],
            ["RED", "GREEN", "GREEN"]
        ],
        "_raw_string": "125\tNamibie\t\n",
        "_file_name": "Flag_Namibie.gif"
    },
    "126": {
        "pattern": [
            ["BLUE", "BLUE", ""],
            ["YELLOW", "YELLOW", ""],
            ["WHITE", "BLUE", ""]
        ],
        "_raw_string": "126\tNauru\t\n",
        "_file_name": "Flag_Nauru.gif"
    },
    "127": {
        "pattern": [
            ["RED", "RED", ""],
            ["WHITE", "RED", ""],
            ["WHITE", "RED", ""]
        ],
        "_raw_string": "127\tN\u00e9pal\t\n",
        "_file_name": "Flag_Nepal.gif"
    },
    "128": {
        "pattern": [
            ["", "BLUE", ""],
            ["", "WHITE", ""],
            ["", "BLUE", ""]
        ],
        "_raw_string": "128\tNicaragua\t\n",
        "_file_name": "Flag_Nicaragua.gif"
    },
    "129": {
        "pattern": [
            ["", "RED", ""],
            ["", "WHITE", ""],
            ["", "GREEN", ""]
        ],
        "_raw_string": "129\tNiger\t\n",
        "_file_name": "Flag_Niger.gif"
    },
    "130": {
        "pattern": [
            ["", "", ""],
            ["", "", ""],
            ["GREEN", "WHITE", "GREEN"]
        ],
        "_raw_string": "130\tNigeria\t\n",
        "_file_name": "Flag_Nigeria.gif"
    },
    "131": {
        "pattern": [
            ["", "", ""],
            ["BLUE", "YELLOW", ""],
            ["YELLOW", "YELLOW", ""]
        ],
        "_raw_string": "131\tNioue\t\n",
        "_file_name": "Flag_Nioue.gif"
    },
    "132": {
        "pattern": [
            ["RED", "BLUE", "RED"],
            ["BLUE", "BLACK", "BLUE"],
            ["RED", "BLUE", "RED"]
        ],
        "_raw_string": "132\tNorv\u00e8ge\t\n",
        "_file_name": "Flag_Norvege.gif"
    },
    "133": {
        "pattern": [
            ["", "", ""],
            ["RED", "BLUE", ""],
            ["BLUE", "BLUE", ""]
        ],
        "_raw_string": "133\tNouvelle-Z\u00e9lande\t\n",
        "_file_name": "Flag_NouvelleZelande.gif"
    },
    "134": {
        "pattern": [
            ["RED", "WHITE", ""],
            ["RED", "RED", ""],
            ["RED", "GREEN", ""]
        ],
        "_raw_string": "134\tOman\t\n",
        "_file_name": "Flag_Oman.gif"
    },
    "135": {
        "pattern": [
            ["", "BLACK", ""],
            ["", "YELLOW", ""],
            ["", "RED", ""]
        ],
        "_raw_string": "135\tOuganda\t\n",
        "_file_name": "Flag_Ouganda.gif"
    },
    "136": {
        "pattern": [
            ["", "BLUE", ""],
            ["", "WHITE", ""],
            ["", "GREEN", ""]
        ],
        "_raw_string": "136\tOuzb\u00e9kistan\t\n",
        "_file_name": "Flag_Ouzbekistan.gif"
    },
    "137": {
        "pattern": [
            ["", "", ""],
            ["WHITE", "GREEN", "WHITE"],
            ["WHITE", "GREEN", "GREEN"]
        ],
        "_raw_string": "137\tPakistan\t\n",
        "_file_name": "Flag_Pakistan.gif"
    },
    "138": {
        "pattern": [
            ["", "", ""],
            ["", "YELLOW", ""],
            ["", "", ""]
        ],
        "_raw_string": "138\tPalaos\t\n",
        "_file_name": "Flag_Palaos.gif"
    },
    "139": {
        "pattern": [
            ["RED", "BLACK", "BLACK"],
            ["RED", "RED", "WHITE"],
            ["RED", "GREEN", "GREEN"]
        ],
        "_raw_string": "139\tPalestine\t\n",
        "_file_name": "Flag_Palestine.gif"
    },
    "140": {
        "pattern": [
            ["", "", ""],
            ["WHITE", "RED", ""],
            ["BLUE", "WHITE", ""]
        ],
        "_raw_string": "140\tPanama\t\n",
        "_file_name": "Flag_Panama.gif"
    },
    "141": {
        "pattern": [
            ["RED", "RED", "RED"],
            ["BLACK", "YELLOW", "RED"],
            ["BLACK", "BLACK", "BLACK"]
        ],
        "_raw_string": "141\tPapouasie-Nouvelle-Guin\u00e9e\t\n",
        "_file_name": "Flag_Papouasie.gif"
    },
    "142": {
        "pattern": [
            ["", "RED", ""],
            ["", "WHITE", ""],
            ["", "BLUE", ""]
        ],
        "_raw_string": "142\tParaguay\t\n",
        "_file_name": "Flag_Paraguay.gif"
    },
    "143": {
        "pattern": [
            ["", "RED", ""],
            ["", "WHITE", ""],
            ["", "BLUE", ""]
        ],
        "_raw_string": "143\tPays-Bas\t\n",
        "_file_name": "Flag_PaysBas.gif"
    },
    "144": {
        "pattern": [
            ["", "", ""],
            ["", "", ""],
            ["RED", "WHITE", "RED"]
        ],
        "_raw_string": "144\tP\u00e9rou\t\n",
        "_file_name": "Flag_Perou.gif"
    },
    "145": {
        "pattern": [
            ["", "", ""],
            ["WHITE", "BLUE", ""],
            ["WHITE", "RED", ""]
        ],
        "_raw_string": "145\tPhilippines\t\n",
        "_file_name": "Flag_Philippines.gif"
    },
    "146": {
        "pattern": [
            ["", "", ""],
            ["", "WHITE", ""],
            ["", "RED", ""]
        ],
        "_raw_string": "146\tPologne\t\n",
        "_file_name": "Flag_Pologne.gif"
    },
    "147": {
        "pattern": [
            ["", "", ""],
            ["", "", ""],
            ["GREEN", "RED", ""]
        ],
        "_raw_string": "147\tPortugal\t\n",
        "_file_name": "Flag_Portugal.gif"
    },
    "148": {
        "pattern": [
            ["", "", ""],
            ["", "", ""],
            ["WHITE", "RED", ""]
        ],
        "_raw_string": "148\tQatar\t\n",
        "_file_name": "Flag_Qatar.gif"
    },
    "149": {
        "pattern": [
            ["BLUE", "WHITE", "RED"],
            ["WHITE", "BLACK", "WHITE"],
            ["RED", "WHITE", "BLUE"]
        ],
        "_raw_string": "149\tR\u00e9publique Dominicaine\t\n",
        "_file_name": "Flag_RepubliqueDominicaine.gif"
    },
    "150": {
        "pattern": [
            ["", "", ""],
            ["", "", ""],
            ["BLUE", "YELLOW", "RED"]
        ],
        "_raw_string": "150\tRoumanie\t\n",
        "_file_name": "Flag_Roumanie.gif"
    },
    "151": {
        "pattern": [
            ["BLUE", "RED", "BLUE"],
            ["RED", "WHITE", "RED"],
            ["BLUE", "RED", "BLUE"]
        ],
        "_raw_string": "151\tRoyaume-Uni\t\n",
        "_file_name": "Flag_RoyaumeUni.gif"
    },
    "152": {
        "pattern": [
            ["", "WHITE", ""],
            ["", "BLUE", ""],
            ["", "RED", ""]
        ],
        "_raw_string": "152\tRussie\t\n",
        "_file_name": "Flag_Russie.gif"
    },
    "153": {
        "pattern": [
            ["", "BLUE", ""],
            ["", "YELLOW", ""],
            ["", "GREEN", ""]
        ],
        "_raw_string": "153\tRwanda\t\n",
        "_file_name": "Flag_Rwanda.gif"
    },
    "158": {
        "pattern": [
            ["", "", ""],
            ["BLUE", "RED", ""],
            ["RED", "RED", ""]
        ],
        "_raw_string": "158\tSamoa\t\n",
        "_file_name": "Flag_Samoa.gif"
    },
    "159": {
        "pattern": [
            ["GREEN", "GREEN", ""],
            ["RED", "YELLOW", ""],
            ["GREEN", "GREEN", ""]
        ],
        "_raw_string": "159\tS\u00e3o Tom\u00e9 et Pr\u00edncipe\t\n",
        "_file_name": "Flag_SaoTomePrincipe.gif"
    },
    "160": {
        "pattern": [
            ["", "", ""],
            ["", "", ""],
            ["GREEN", "YELLOW", "RED"]
        ],
        "_raw_string": "160\tS\u00e9n\u00e9gal\t\n",
        "_file_name": "Flag_Senegal.gif"
    },
    "161": {
        "pattern": [
            ["", "RED", ""],
            ["", "BLUE", ""],
            ["", "WHITE", ""]
        ],
        "_raw_string": "161\tSerbie\t\n",
        "_file_name": "Flag_Serbie.gif"
    },
    "162": {
        "pattern": [
            ["BLUE", "YELLOW", "RED"],
            ["YELLOW", "RED", "WHITE"],
            ["RED", "WHITE", "GREEN"]
        ],
        "_raw_string": "162\tSeychelles\t\n",
        "_file_name": "Flag_Seychelles.gif"
    },
    "163": {
        "pattern": [
            ["", "GREEN", ""],
            ["", "WHITE", ""],
            ["", "BLUE", ""]
        ],
        "_raw_string": "163\tSierra Leone\t\n",
        "_file_name": "Flag_SierraLeone.gif"
    },
    "164": {
        "pattern": [
            ["", "", ""],
            ["", "RED", ""],
            ["", "WHITE", ""]
        ],
        "_raw_string": "164\tSingapour\t\n",
        "_file_name": "Flag_Singapour.gif"
    },
    "165": {
        "pattern": [
            ["WHITE", "WHITE", "WHITE"],
            ["BLUE", "RED", "BLUE"],
            ["RED", "RED", "RED"]
        ],
        "_raw_string": "165\tSlovaquie\t\n",
        "_file_name": "Flag_Slovaquie.gif"
    },
    "166": {
        "pattern": [
            ["", "WHITE", ""],
            ["", "BLUE", ""],
            ["", "RED", ""]
        ],
        "_raw_string": "166\tSlov\u00e9nie\t\n",
        "_file_name": "Flag_Slovenie.gif"
    },
    "167": {
        "pattern": [
            ["", "", ""],
            ["", "WHITE", ""],
            ["", "", ""]
        ],
        "_raw_string": "167\tSomalie\t\n",
        "_file_name": "Flag_Somalie.gif"
    },
    "168": {
        "pattern": [
            ["RED", "RED", "RED"],
            ["GREEN", "WHITE", "WHITE"],
            ["WHITE", "BLACK", "BLACK"]
        ],
        "_raw_string": "168\tSoudan\t\n",
        "_file_name": "Flag_Soudan.gif"
    },
    "169": {
        "pattern": [
            ["BLACK", "BLACK", "BLACK"],
            ["BLUE", "RED", "RED"],
            ["GREEN", "GREEN", "GREEN"]
        ],
        "_raw_string": "169\tSoudan du Sud\t\n",
        "_file_name": "Flag_SoudanSud.gif"
    },
    "170": {
        "pattern": [
            ["GREEN", "RED", "RED"],
            ["GREEN", "YELLOW", "YELLOW"],
            ["GREEN", "RED", "RED"]
        ],
        "_raw_string": "170\tSri Lanka\t\n",
        "_file_name": "Flag_SriLanka.gif"
    },
    "154": {
        "pattern": [
            ["", "", ""],
            ["GREEN", "BLACK", ""],
            ["BLACK", "RED", ""]
        ],
        "_raw_string": "154\tSaint-Kitts-et-Nevis\t\n",
        "_file_name": "Flag_StKittsNevis.gif"
    },
    "155": {
        "pattern": [
            ["", "", ""],
            ["WHITE", "YELLOW", "WHITE"],
            ["BLUE", "GREEN", "BLUE"]
        ],
        "_raw_string": "155\tSaint-Marin\t\n",
        "_file_name": "Flag_StMarin.gif"
    },
    "156": {
        "pattern": [
            ["", "", ""],
            ["", "", ""],
            ["BLUE", "YELLOW", "GREEN"]
        ],
        "_raw_string": "156\tSaint-Vincent-et-les-Grenadines\t\n",
        "_file_name": "Flag_StVincentGrenadines.gif"
    },
    "157": {
        "pattern": [
            ["BLUE", "BLACK", "BLUE"],
            ["BLACK", "YELLOW", "BLACK"],
            ["YELLOW", "YELLOW", "YELLOW"]
        ],
        "_raw_string": "157\tSainte-Lucie\t\n",
        "_file_name": "Flag_SteLucie.gif"
    },
    "171": {
        "pattern": [
            ["BLUE", "YELLOW", "BLUE"],
            ["YELLOW", "WHITE", "YELLOW"],
            ["BLUE", "YELLOW", "BLUE"]
        ],
        "_raw_string": "171\tSu\u00e8de\t\n",
        "_file_name": "Flag_Suede.gif"
    },
    "172": {
        "pattern": [
            ["", "", ""],
            ["RED", "RED", ""],
            ["RED", "RED", ""]
        ],
        "_raw_string": "172\tSuisse\t\n",
        "_file_name": "Flag_Suisse.gif"
    },
    "173": {
        "pattern": [
            ["GREEN", "GREEN", ""],
            ["RED", "YELLOW", ""],
            ["GREEN", "GREEN", ""]
        ],
        "_raw_string": "173\tSuriname\t\n",
        "_file_name": "Flag_Suriname.gif"
    },
    "174": {
        "pattern": [
            ["BLUE", "BLUE", "BLUE"],
            ["RED", "RED", "RED"],
            ["RED", "BLACK", "WHITE"]
        ],
        "_raw_string": "174\tSwaziland\t\n",
        "_file_name": "Flag_Swaziland.gif"
    },
    "175": {
        "pattern": [
            ["RED", "RED", "RED"],
            ["WHITE", "GREEN", "WHITE"],
            ["BLACK", "BLACK", "BLACK"]
        ],
        "_raw_string": "175\tSyrie\t\n",
        "_file_name": "Flag_Syrie.gif"
    },
    "176": {
        "pattern": [
            ["", "RED", ""],
            ["", "WHITE", ""],
            ["", "GREEN", ""]
        ],
        "_raw_string": "176\tTadjikistan\t\n",
        "_file_name": "Flag_Tadjikistan.gif"
    },
    "177": {
        "pattern": [
            ["GREEN", "GREEN", "BLACK"],
            ["GREEN", "BLACK", "BLUE"],
            ["BLACK", "BLUE", "BLUE"]
        ],
        "_raw_string": "177\tTanzanie\t\n",
        "_file_name": "Flag_Tanzanie.gif"
    },
    "178": {
        "pattern": [
            ["", "", ""],
            ["", "", ""],
            ["BLUE", "YELLOW", "RED"]
        ],
        "_raw_string": "178\tTchad\t\n",
        "_file_name": "Flag_Tchad.gif"
    },
    "179": {
        "pattern": [
            ["BLUE", "WHITE", "WHITE"],
            ["BLUE", "BLUE", "WHITE"],
            ["BLUE", "RED", "RED"]
        ],
        "_raw_string": "179\tTch\u00e8que, R\u00e9publique\t\n",
        "_file_name": "Flag_Tcheque.gif"
    },
    "180": {
        "pattern": [
            ["WHITE", "RED", "WHITE"],
            ["BLUE", "BLUE", "BLUE"],
            ["RED", "WHITE", "RED"]
        ],
        "_raw_string": "180\tTha\u00eflande\t\n",
        "_file_name": "Flag_Thailande.gif"
    },
    "181": {
        "pattern": [
            ["BLACK", "RED", "RED"],
            ["WHITE", "BLACK", "YELLOW"],
            ["BLACK", "RED", "RED"]
        ],
        "_raw_string": "181\tTimor-Oriental\t\n",
        "_file_name": "Flag_Timor.gif"
    },
    "182": {
        "pattern": [
            ["RED", "RED", "GREEN"],
            ["RED", "RED", "YELLOW"],
            ["GREEN", "GREEN", "GREEN"]
        ],
        "_raw_string": "182\tTogo\t\n",
        "_file_name": "Flag_Togo.gif"
    },
    "183": {
        "pattern": [
            ["", "", ""],
            ["WHITE", "RED", ""],
            ["RED", "RED", ""]
        ],
        "_raw_string": "183\tTonga\t\n",
        "_file_name": "Flag_Tonga.gif"
    },
    "184": {
        "pattern": [
            ["", "", ""],
            ["BLACK", "RED", ""],
            ["RED", "BLACK", ""]
        ],
        "_raw_string": "184\tTrinit\u00e9-et-Tobago\t\n",
        "_file_name": "Flag_TriniteTobago.gif"
    },
    "185": {
        "pattern": [
            ["RED", "WHITE", ""],
            ["WHITE", "RED", ""],
            ["RED", "WHITE", ""]
        ],
        "_raw_string": "185\tTunisie\t\n",
        "_file_name": "Flag_Tunisie.gif"
    },
    "186": {
        "pattern": [
            ["", "", ""],
            ["RED", "WHITE", "GREEN"],
            ["RED", "GREEN", "GREEN"]
        ],
        "_raw_string": "186\tTurkm\u00e9nistan\t\n",
        "_file_name": "Flag_Turkmenistan.gif"
    },
    "187": {
        "pattern": [
            ["RED", "WHITE", ""],
            ["WHITE", "RED", ""],
            ["RED", "WHITE", ""]
        ],
        "_raw_string": "187\tTurquie\t\n",
        "_file_name": "Flag_Turquie.gif"
    },
    "188": {
        "pattern": [
            ["RED", "BLUE", "BLUE"],
            ["BLUE", "BLUE", "YELLOW"],
            ["", "", ""]
        ],
        "_raw_string": "188\tTuvalu\t\n",
        "_file_name": "Flag_Tuvalu.gif"
    },
    "189": {
        "pattern": [
            ["", "", ""],
            ["", "BLUE", ""],
            ["", "YELLOW", ""]
        ],
        "_raw_string": "189\tUkraine\t\n",
        "_file_name": "Flag_Ukraine.gif"
    },
    "190": {
        "pattern": [
            ["YELLOW", "WHITE", "BLUE"],
            ["WHITE", "WHITE", "WHITE"],
            ["BLUE", "BLUE", "BLUE"]
        ],
        "_raw_string": "190\tUruguay\t\n",
        "_file_name": "Flag_Uruguay.gif"
    },
    "191": {
        "pattern": [
            ["BLACK", "RED", "RED"],
            ["YELLOW", "BLACK", "BLACK"],
            ["BLACK", "GREEN", "GREEN"]
        ],
        "_raw_string": "191\tVanuatu\t\n",
        "_file_name": "Flag_Vanuatu.gif"
    },
    "192": {
        "pattern": [
            ["", "", ""],
            ["", "YELLOW", ""],
            ["", "WHITE", ""]
        ],
        "_raw_string": "192\tVatican\t\n",
        "_file_name": "Flag_Vatican.gif"
    },
    "193": {
        "pattern": [
            ["", "YELLOW", ""],
            ["", "BLUE", ""],
            ["", "RED", ""]
        ],
        "_raw_string": "193\tVenezuela\t\n",
        "_file_name": "Flag_Venezuela.gif"
    },
    "194": {
        "pattern": [
            ["", "", ""],
            ["", "", ""],
            ["RED", "YELLOW", "RED"]
        ],
        "_raw_string": "194\tVi\u00eat Nam\t\n",
        "_file_name": "Flag_VietNam.gif"
    },
    "195": {
        "pattern": [
            ["", "RED", ""],
            ["", "WHITE", ""],
            ["", "BLACK", ""]
        ],
        "_raw_string": "195\tY\u00e9men\t\n",
        "_file_name": "Flag_Yemen.gif"
    },
    "196": {
        "pattern": [
            ["", "", ""],
            ["GREEN", "GREEN", "YELLOW"],
            ["GREEN", "GREEN", "BLACK"]
        ],
        "_raw_string": "196\tZambie\t\n",
        "_file_name": "Flag_Zambie.gif"
    },
    "197": {
        "pattern": [
            ["WHITE", "GREEN", "GREEN"],
            ["WHITE", "WHITE", "YELLOW"],
            ["YELLOW", "BLACK", "RED"]
        ],
        "_raw_string": "197\tZimbabwe\t",
        "_file_name": "Flag_Zimbabwe.gif"
    }
}


class CompetitionFlagRepository(FlagRepository):

    def get_flag(self, flag_code: int):
        stored_flag = FLAGS[str(flag_code)]
        pattern = []
        for row in stored_flag['pattern']:
            pattern.append([x for x in map(lambda x: CubeColour.from_string(x), row)])
        return Flag(flag_code, pattern, stored_flag['_raw_string'].split("\t")[1])
