package org;

/* iMan created on ۰۷/۱۲/۲۰۲۰
inside the package - org */

public class Main {

    /**
     * @param a
     * @param b
     * @param c
     * @return min value of a,b,c
     */

    public static int min(int a, int b, int c) {
        if (a <= b && a <= c)
            return a;
        if (b <= a && b <= c)
            return b;
        else
            return c;
    }

    /**
     * @param aminoAcid1
     * @param aminoAcid2
     * @param aminoAcid1Length
     * @param aminoAcid2Length
     * @return Store Table ( Dynamic Programming ) = EditDistance
     */
    public static int editDistance(String aminoAcid1, String aminoAcid2, int aminoAcid1Length, int aminoAcid2Length) {

        int storeTable[][] = new int[2][aminoAcid1Length + 1];

        for (int i = 0; i <= aminoAcid1Length; i++)
            storeTable[0][i] = i;

        for (int i = 1; i <= aminoAcid2Length; i++) {
            for (int j = 0; j <= aminoAcid1Length; j++) {
                if (j == 0)
                    storeTable[i % 2][j] = i;
                else if (aminoAcid1.charAt(j - 1) == aminoAcid2.charAt(i - 1)) {
                    storeTable[i % 2][j] = storeTable[(i - 1) % 2][j - 1];
                } else {
                    storeTable[i % 2][j] = 1 + min(storeTable[(i - 1) % 2][j], storeTable[i % 2][j - 1], storeTable[(i - 1) % 2][j - 1]);

                }
            }
        }
        return storeTable[aminoAcid2Length % 2][aminoAcid1Length];
    }

    public static void main(String[] args) {

        String aminoAcid1 = "QGVFITSDSFWFPYKIHPEFLCRDDYLNEDLYIDQVELNDCFDEIKPTLSYPNYWQTGAYGWEIDDRSKGDEYSNQSMDRIPWGESWAWTSTNEGTQDPPSILVVIRHRSGYPSVPRVGMTTVSIMVRQNFGEGKKEFPFAQEPAVLIFHLEHCNRDIETDMCWYIWTNVDLDHEMEVTSQNIYYARDVAQEFWRTPRRVGMYFWCCLSDQWGDRDDFNTFRPMGYEKDFPFNVYCIKSKFFMHWLNDETFMMTNPEPFNVNWVQANIMTQSQQDVCGSFHMWQAHTPWVKAKISNSVNGGPFHIELNGWNTELQHINNSLILWMVFHQTELCFYKWSEIMRGDWPPLWGAFIWESDAYENAFAYIYCMNLLHLKWQQINSMVFSAVLNPVECYFLLFFQRYEMCCAALWKSMEFWGTHKDGPQDNQFRLHPLRLFQSYTMWRCLWYMSEGTCQTNGLAGRCDDYMTGALSVTNWNACLIPKVDADAKPRCRWEQRQSEWQTHRSWFRVDSCDAMVELMSCCRHAKDMIVLDANKVKVVLYSWTVTQFVRDTMIGNFDLKSAEEGKEHQNLCIWPTSYEVEIRWFMMQWEWDAWVVVKTFLQDGQPDQLFVRFDAAIKDGEEIYRVKNAGHFKMVSLKQMYTMHINVEFQGDWMFAYKFHECYACHHWNWIQPQNSQCQYEGVQLWWQAPPSPWNQGGTRHKEQDWGRSKEGYCCSNLSPCKPHITAVPRTSSACTMFLQVYRFHCNEHYFAWHTMYKKLHRYNEECPLRNENMTWFHIPPFKSQQVFVHDIREFKDWEVYRMAETIEPPTNWTTDKPIDEQDYIMNWNRCTYVDPPGADSHIIETHGVKYMRSKYMECGTEHAGDVIMWPQHTLKPGGYCIVSSNTCVDSNEHNMNVFKNCWFHIWFKLARSGNFLACGKQTCFWQPGDMIGEFMCVGQDARKHPFIFTNHWSWYSHSVFSVAMDPQHECPLPSYHPRNMYSCYCVLHKCQEMYQNKFSPMKMWGNEFVVDEMCYDWEENFSKLAEQNATDTASFGTSCHCMPSDLKNQARNIMINAKWPYQRITTCTTFENKAWCRREGMTNTYDWFYLEKNFHFLPTCLRVCYPRQITRKSTMMDHEFRCKYYIYNYQPPNFCQLLVHLSSFYVEVDNAILMQQPGPSQKLYCWQQNHTMYYHNQDKTRYRLFAEEPKYHLGFNLYWKNIKAEGETMPFTLMPGPHGFMQVWIGAMMDASNMYGKEEAMSHNGTYTPCGTQKMQGQAAKYDMHYKDISLYMHGYCWCTAKPFECQYESVIGSDPSKKRSTRDRVPFSPAMTDDIQKRTWPTVTYYQSTMNDGIDRVGGGWNHCVQFKQWMTLHWANQGTNVPMYEAPRCVPGGVYPIGDVPNPIEDFEQVDYTTQTLWTQPQDAKAQTVNRKYYMSTGAIVWRSILPYAMRPRPRDKPTVTIAVDGNNHLGQQQHKPLSKTRRSMVKGAKPTVRCMHNWWCETIMCENMEIQQKGQGLFCPYPHLLDNQDQECSQDHHYTAQPEWAHVPWQEHIGFYDTIEGDQPPPPQKQEIHFDRCMWFICQYWNESEPNSFTMRHVPHFLMQSDNFCQGRSLHNYFDWPGYNCCCQEWTGSHIMDGVPEGNANVTDNVEMSFFLGIVANSPSYNENWYCHSNTEVQVEQEGWRRVGCYIHEDHTLVAHGLKQTEGFNNPYWGQTYWFYMRHFNYQLAWRWCTKMGSYQDYVHGLDRIVNCCPCRSRPVESGYDMKFANNKTIMNLVDDDYQYRWYQWIHWRGFSLREADWLVSLWVCLTARTYQIEEWQLDQVHMPDTWWTLLMHQPMNKEETQIMTAFLACLAHMDCIFMRAGSRAECHMGDNEIQSVTDNYFIWFGSCRHVTRAESFSQVVKLNAPIHSALQFETVFDGFFMYIFQTHKSHDQLYQCMQSPRCKPPKWFECTWVSCIDPCSTKPFPDRAQRFGHLSADEYEWYMASKFCRKRDKKDSNGTFCTERTRDENMESKDNLIIGNRHWWKEMQAHFRRCEGEATSYSTRFIEPRGCVLPPWWGCHNREKFALTINRLWIMDGFSPTKWDKPRSVQITDIDRVNDGLCDCWTYMTEVGSDELKVMRNTSYLFECWHQNIYHWPGQPEELVFKQHGFGGYHPLSELQGREDPRGECNTYLVECRDSWNFGHSFAMFDNCSTERPTCFFKGCCCTHGQNHLCSVNYAFPVDYNCACNFIYGFHKWFMAIVEHVCHKQFNHTGQRHQDVMQQDMTLYHNHYWIVWHAFGNIFPYHCLWTMLEHLKRLPDWHFGKFLFDHVFHITIACGVSWGKMFWQKVKGKSYEALIDTAGVRDYGKCFADCYGSCCCNKNIGNREQMKDDDHWQFLSYLVDYKYYYWCQIHEIMHGAWDIQRHINTRNWADLLEVIFRLCWTPNGILVPNYYVLAVMVMIFPLRGNPAAYWYGQNCQAELMYLDRNENIYSEESMDISYPDPHLINHWCDHVGICFPHEETSWDCFIWNYSWPEAWTTWGCPKIQHITMDDWLHLWYRAYEINKMNMFMVWLHGKFRVDECKKCFLSPYTRLTNAMMQAESHIFAEYVWDKTSDNITNRYYVKVGESKFYPKCFVCRVVSLTDTIDDRSEPPTLDHLAVSNALAGPAEMLTFYGDYHIDLEANYNMQHQLDNGRVRCRINQMWTWLMMADYQRHMPLHEKIQPCQNAMGRWTLMQVRDGWWLKWALPADFRMAQSQYACPTGLCMDMWLMEIVGWQQGPIISWRNVFSGDGPDVKQALCGPQSHERKEKVSHPVSIFFRMEACVREVTPKQAAKPCWNYCRQAAQWKCWCNNPVMQWLYHLTDIMLINRPKVIKQITKRMIHATVPLLSYVKCTKPWNPYATLYKQIYMELQFGIMPVTIPLEMSNSAQECDWGGHESEIWPERMHNLSQEMVVAKMPDKDELLTAESDLCILPEQCFETVMMILRSTMYVPQAMFFSNCEHAPYALQWEWKTLFVDHIIIFTQWTHRNMIVYYNNIKFSAECQWIYWCMSCTMAISYNGEEHEWINYIWMDFEWSLEEQFWYEPDKETGSECRMLPFDFIPHCHFSDPEDYVTLTILCIITHQPNICALRFNLTEYVGQLTTCPNRYLAPSIWANDELATVHSKVKKIIGLMGPVPDEPHDYRIGMPLKLMEKMPEWRVYYAKCIDVYCTMFMGMWTYWCVEGESPWSMNKGIAAYYICKAHDAENRSSDPIMIPIDDCMNAGGDIPLWKFYAYFWALSIARTWSQAGMKHIMMWNCKPRRIHKNLRDLHLRWSWCPNYFSYESFVAIDNWDTQRSMGHFNWVKANDVPLDATPKSTSDQMACQEHRWRFVGRQIMQWMMESRTINFRVEGCLLEINQPIQKDQMQAEKKHCICNYKFHVMYSRFQESNYDRGAAMNPPAGEGRVYDYNLTWNREQEMEHHNKMVDWLSGVGCEGGITIRRNLMFQMNQLELLKSWQTHQKNNFPDFIWHTMQQFTNTRRDTIDMDKGWPEVTSSLNHWPSYTMTPTAVQYSVELAHRETWRQQNHNQRGWICGEFDEPNWDHNKSWHSPFVTIYVFENWNLMKCAWQAAHMYVNEGYDHIHPGRCQNWIADMHEYLEADHFKLDETGIPYKETVVTCIPEHGIVSSARNQMRKNINKCTCNVVWHKQWRCGPETTVCGCSKMQARWIRDRAHFSKALDICKSIFDQVIEVCGQPKDASFPLPPEQVAHKHIQSALGIYMQKCLYNRRAWSHVLNYWTSDEKYIWFANVTLTRYHMMNPPLENKPLHDHGCYMEYNNDVTSMCNADPDRFRNWRVGQYNHMAYCVYYKALNSKPYNNHQKLHPAVPRMWRVTIPQDVGHFIGEQIADGWAMMMMHLYNTRCGDFHKSGTTDYHDSAEHPLIRTTVTHWGEEQTHNETHMYHEKMVHYQGHQRQVKVSPEIVNNFTKKNCDGYMSRMIGWFLEFWVAAVEHFMARHAWGHAVVMKQHYWNFMQHCCCGSQCSDCWWDFFCPWFWNWPRAWGRTMRLKNETGVTKRTAPTRAQWTCPKMTDWFEEVRNKKNDLALKKIGTEHVGRACGGPNWPEWELAEREGVWKKADYLWKQSMNTAQMASYGGMWLACMQPWPFACWMAPRAHPECLNKRCVIYWACVPRSIYMEMMHTWVFEKMMPSHEVSRWPGPIPPIVLYTIVLQRNAMQINPRAPYVHKSQNSWMNDNVYNGGIIPQHTWFSFEEERTSCIYIMASFRQAADCIGQDRRGDCATACFQMGLDDHYTWKWSIAKLCPKLVHVSLSTYRHPSPCWNWRNISTFIKMQGCISSIPNCYEAAHHPTSLDAGQSQQCYDKRIVLQCPYDEPISFACGQMVKCWPNHFAVYQSQYA";
        String aminoAcid2 = "QGVFITSDSNWFPYNFMRIDAEIHFLCDYLVELNYYACFDIIKPNLTAYPNYWPEYKTDYTMAYGWEIDDRSYEYWFWPPYQRHRKIQSMDRIQCISLYVPWGESWAWTSISNEGTEDPPSILVSPSDPTVFCIRHRYRSGPIAGYPSVPRVGMTTVSIMVRQNFGEMKDWAAYNAREFPFFHVETDMDIEMEHCSRNIYYARDEAQERVQMYFWYCLWKPIYPGDAHFFIHRGFNTFRPMNAHKVIIFHLWLYCILHDAIGLVCETFGHTNPYPFNVNWVQANIMCAFFDLVMWQSQQMVCGSFHMWQAHTPIVKAKISVLVNPEMVPNGQNRALGIELQHKNNSTNYCFIQIYEYNEVKWSEIMRGDWGAQHRLPFPAEFWESFSYYFRGWYENAFAYFKRHYIFCPCMNFGEQQELHLKIQQINSMVFSAVLNPVECSDFLLFFQRYQMCCAALWKSSEFPGLVNTFTGRLSMPLRLFQSYTMWECLWYMSEPTCQTNGLASVTNWVDADAQSEWQTHRSWFRVDECDANFSAKHAVELMSCCRHSKDMGANVVLYSWTVTQFVRDTMIGNFDLSAEGYTFTLPTSYKVEIRDAWVQVKTFLTDGQPDQLFVRFDAAIKDGEEPGENPPIGHFMMVSINVSFQGDTPERLQVQHFHEWYACHHWGWIQPQNSQCQYEGGTVPDVQLWWQAPSPWNQIWEMHINDGDYQRSSHDWGISKEGCCNQAPCKPHIGILMSASADTMFLEWHTKQHRTQGEEPTFQPLRNENMTQVFSHDIRTIFKPISEQWYIWNTCTYVDPIIETHGVKYMKYIYWKPECGTEHAGHWIMWPQFYHQAIHEMVIVSSNTCVDSNEHNMNVAKNCWFCHGIWWHPIWAKLARCSKMPAGQQLSYATVCGKQTCFWQPGDYNQVCEDYFIGEGQYLHEATFYMFFRPAVNHWSVYSYSVFSECPLDFNCSCISYHKCPKRWCLNNPLHNYSIHGWRGHRNYCVLHKPQEMYQNQLEKKEFSGNELISWPRRYVVDEMCEKWEENFSAPGPPKWAENATDTGETETPSPFDYDKGECTKNQARNIMTNAKWPYQRITTCTTFRNKAWCRREGFTNPYDWFYLEKNFHFLRKSRTCLKETRTSLMMDQQQDMVMCFRCKYYIYNYQPPNFQLLVHLSSFYFHYITKLDVSSQKNQYCWQQNHTMYYHNQDKTRYRLFAEEPKYHLGANLYWKNIKAEGETYPWYNEYWFGTWLGMPDAHGFYQVWDGMMMDALHWYLWLQNMYGKEEAMSFNGTYTPSGTQKMQIASQNAKYDMHGYCWCTAKPFCTWDQYYSVGGSDISKAMSTRDRVPSSPARTQKRIQVIPTVTYYQNDGIDRVGSHDFPVWTYHTGDCWNHCVQQRCDSQRMTLHWACQGTNVAPRCVPGIHHIHDPVVYPNPIEDTEIQVDYDDDQYQDQQWLLWTLTVNRKYYIQVDAEVEMTEYRSILWAGYWNSRYAMRPRPRDKPGFAWYISYVKIAVDGNNHQGDQQHKPLRSMPWYTMLNAKPTVRRMHNWWCTTPCDMFQGLDCLYPHLCSQDPEWAHKPWQEHIGFYDTIEGICHAQPPSMWFICRYTNERENNSFTMKHVPHDLMHDWTMNRWNSDNFNIGPQGRSLHNYCCQEWTAEEHIMDQAVTRCQGWNVNVSFFLGIVANSPSYNSNPYCHSEVQVEQEGWRRVGCYPSYWTLVLKGETDTEGFNPMNVASPYWYSWWQHRAQTYDFEMRHFNYQLARRWCTKMKPVRAMDWGSYSYVHWLDVCYFNIHNCYECFSQNGPCRSRGFWQRVGWEGWEFDMNLVRWYQWIHWRGFSCREAIWLVSLWVCLNARTYQIEEWQLDQVHMPWWTLLMHPISWEETQISFWTDVCWHYKTFLACLAHMDCIFMRAGVWYFIWFGSVRHVRAESARNKRVLFETVFKMKTHKSHDQCKPPKWFECTWVSCIDVATQWPVFCSTKPFDEYEWYQASKFCMKRDKKDSNCTFCTERTRDENMSSKQNFLYSPLFIGNRHIVKEMQAHFRRCEGEATSMSTRPRGCVLPPNWCCHNREKFALCMTILPVWYRLWIMDGFSPTKWDKPRSVCIIDPTDNGDRVNDGLCDCWTHMTEVPSDELKVMRNTSYLFECPCQNYHWPGQPEEMVFKQHGFGGYHWEQYLYGHPLQGGEDPRGECNMINLGVNVMGPGVGHSFAMFDACSTERPTCFFKKCKRISACTVNYCACEFIYGFHSWFMARVEHVCHKQFNHTGQRHWDVMSHMNLNNDMHLRCTWCQKTHLHYWIPWHAFGNIFWTMLEHLKYAPDWHFGKFAKITFDGPIHGHWSITIAGTPWHRRGVSVCAGVRDYGKCWADCYGKCLCNHNIGNHWQFLSYRVDYKYFYHAEAMQLNHINTRNWLLEELDITMGVGGHEGENCVAVMVMIFRLRGTQCSIPPAAINQAFDELMYNIYSEENHDISYNHDCDHVGICTPHEETSWDWFIWNYSWTIYNAAWTTWGCCLYAIWDLLHLWYDAYEVNQKYMNMFMQSRMLMRWTWLNGECKKCFLYTRLTNAMMQWESHIFAYYVWDKTSDNITNRYYFYPSLTDGEPDEDMTKCHCRNRIEDHLAISNALAGPAEMLTFYGDYIIQHQLDNGRVRCRINQMWTMMADQQRHMIVICTPAYCDLWQAAGRCTLMCQTASIEIKWLKWFLPHLPADFRMALITAAGLSQYGTTCDTGLELCNKQAWTMDMWLMEIVGWPNYQQIWIISWRNVFNASGDGPDVKAALCCPQGHEGKEKPSHPVSREYRPKQAAKPCWNYCRQAYTCWWPWEYCCWCNNPVMQWLYHLTDIMSTYMNRSIVIKQPTKCMIHATVPKCTKPWNPYAQGHCTGALACLQFGIMPVTCCLEMSNNQHQECDIPCTKHESEIWPERMHNLSQESVVAKMPDKVKQWRKCVFELLTAELDECILPEFCKIYHFETKEDYKMFFSFMWCPAEHAPYSCEWRGTEVPWGTLFVDHIIGYMHWTLFVTQWTHRNYYANIAFSAECQWIYWCMQSCTMAIEQLFITCMDFPEFAEWLEEQFSEDRMLPNALQFELGWDTEDYVTNTEDISYQVMTCPVHTALRFNATEYVRMVNMMGSQSTTCPNRYLAPSIHVKKIIGLMGPVPDEWHYYRIGMPLKLMEKMPAWRVYYSYLMCTCIDVNCTMFSGYWCVQGMNEWGGGGIAAYYICKAHDALRAMTSNRVSDPIFILIDDCMNAGGDHMRPVFLWKFYAYFWALSIARTWSQAQMKHIMMHACLKPNLRDLHHMWNYFSYESFVAIDNWYCFVPWCQMERVEGVFQLYYVLHATNKSTSDQMEHRWQSAKVTKTNFRVETSASLILRQDLLEKHCICNYKFHVMEGNVELYFQCWNVGTRNHVYDDLRGGGRLTWNREVYKEMPPMEHHNKMVDWLSGVPETSNITYMRRNLLRSWQTHQKNNFPKEYATPIWHTMQQFNTRRNTIDMHYWDNKGWPEVTSTMTPTAVNDSDNIEPGDQVPPHTAHREDNWIQQNHNQRGWICGEFDMPNWDHNKSWHSPFVTIYVFEAWQTADTPIPLMYVNEAMSWPDHIHPGRCQRWITDMKEYLEADHFKTKAETTVFESWLQMHRFSAMEPKIPSKHHVSSWGTVSSASNQMPLRMIYKIGKLINNMWDYSMNFGIPKRCYQDLLSWYAWRAHMPRKMAMGPETTQCGCSMMQWKSIPMDWIRDRAHFDPPGKSIVTYKMGWRDNDRMHWVIEVVYQPKDASFPLPPEQIAECDAHKHFFHCLWYPYKCLYNRKKKDHFCAWSHVLNYWDMHKMSDYPAMSCYILFANVTQTRYHMMNPPLDNKPLHDHGCYMEYNMDVSAMCNWRVGQTCPMWDANHMRYCVYYKANNSKMRPDNNDENDQPSQTPPNRLHRAVPRMWNVTDPQDVGHWAMMKFIVSYKHMWLYRPPDTDYHDSMQSSTRNFWLIRTTVTHQGEEQTHYETHMYHEKMVHYSPEIVNNFTKKVWWMRLCDGYMSRMFWVAGAMIRMEWVVHHFMQHCCCGSQCKATNCKILWECPPPWDCFCSWKVACSGIQDMTCTNGVCCRTAPTNEFAQSTCPKMPDWFVWEVRNKKYNNMRQVETDVDRALKAIGTEHVGRACGLPNWEDYLSKQSQMASYGQMWLGAFNWRWIEGMQTQPFEFDFNMCWMARDKQCSYMSWCPHAHPECLKKRCVIYWACVPRVLIRMDAIYMEMMHTEMMQTHQYHPSSRWPGPFPPRNAMQINQNIGGGIIPQHTWLWKREFQQSFMDDCEFRIYIMDEFDCIGQDRRGFRSVGWLVQCDQMGLDDHYTWKWSKAKLCYKLVHVSLIFYRHPSCITCSYRMEPIIWGGCGANSSDPNCSERKHCEAAHTSLDAGQQQQCYDKRHVLQCPYDEEWSYYYTKCWPNTFAVYQSQYA";

        int aminoAcid1Length = aminoAcid1.length();
        int aminoAcid2Length = aminoAcid2.length();

        System.out.println("First Amino acid is : ");
        System.out.println(aminoAcid1);
        System.out.println("Second Amino acid is : ");
        System.out.println(aminoAcid2);
        System.out.println("Edit distance = " + editDistance(aminoAcid1, aminoAcid2, aminoAcid1Length, aminoAcid2Length));

    }
}