import pyldavis_dash
import dash
import dash_html_components as html

app = dash.Dash('')

app.scripts.config.serve_locally = True

app.css.append_css({
    'external_url': 'https://cdn.rawgit.com/bmabey/pyLDAvis/files/ldavis.v1.0.0.css'})

data = {"mdsDat": {"Freq": [51.097304691503076, 48.902695308496924], "cluster": [1, 1], "topics": [1, 2], "x": [2352.8154296875, -2352.815185546875], "y": [-5514.8720703125, 5514.8720703125]}, "tinfo": {"Category": ["Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2"], "Freq": [25.0, 19.0, 19.0, 18.0, 16.0, 15.0, 15.0, 13.0, 13.0, 12.0, 24.869411820883208, 18.13084877581997, 18.867486917997518, 18.86705283331816, 16.395267585120024, 10.547731897736899, 12.9801211239908, 10.518601998956003, 9.694935673550674, 10.473133010662341, 13.378201437591123, 15.044039765341125, 14.992009910920267, 13.31480491101705, 11.644856878684358, 11.586049499009286, 10.728419167690946, 9.05075824320389, 9.851035652573522, 9.827550427069491], "Term": ["relever", "acces", "operation", "virement", "jour", "espace", "prelevement", "depense", "trouver", "moment", "relever", "virement", "acces", "operation", "jour", "code", "page", "demande", "idee", "service", "depense", "espace", "prelevement", "trouver", "moment", "ligne", "credit", "carte", "document", "banque"], "Total": [25.0, 19.0, 19.0, 18.0, 16.0, 15.0, 15.0, 13.0, 13.0, 12.0, 25.373697845237697, 18.6097474353762, 19.457587217831907, 19.457596853836225, 16.9198906311669, 11.000352803449125, 13.538933556494536, 11.000999441867895, 10.155091549640005, 11.002008782645737, 13.817324202814289, 15.544349943081633, 15.543220043302897, 13.815947460131712, 12.088832471982533, 12.087555388930452, 11.223505881842131, 9.496223397642183, 10.359027407226389, 10.358517393285418], "loglift": [10.0, 9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0, 0.6514, 0.6454, 0.6406, 0.6406, 0.6399, 0.6294, 0.6293, 0.6266, 0.6251, 0.6222, 0.683, 0.6826, 0.6792, 0.6784, 0.6779, 0.673, 0.6702, 0.6673, 0.6651, 0.6627], "logprob": [10.0, 9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0, -3.0386, -3.3546, -3.3148, -3.3148, -3.4552, -3.8963, -3.6888, -3.899, -3.9806, -3.9034, -3.6147, -3.4973, -3.5008, -3.6194, -3.7534, -3.7585, -3.8354, -4.0054, -3.9207, -3.9231]}, "token.table": {"Topic": [1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1], "Freq": [0.9764828386629277, 0.051393833613838306, 0.0965389120887337, 0.9653891208873371, 0.9477451849157855, 0.9999679279878174, 0.980085912174401, 0.9999091499028632, 0.940847866720257, 0.09653415911443643, 0.9653415911443642, 0.06433205657757807, 0.964980848663671, 0.9847277054193073, 0.9456325899960348, 0.05910203687475218, 0.082729713976391, 0.992756567716692, 0.9926516913698313, 0.9764823550783968, 0.05139380816202088, 0.9601937956009827, 0.07386106120007559, 0.06433673313599325, 0.9650509970398988, 0.9852722355441844, 0.039410889421767376, 0.9089249243077976, 0.09089249243077975, 0.0723801246990604, 0.9409416210877851, 0.9672350504759081], "Term": ["acces", "acces", "banque", "banque", "carte", "code", "credit", "demande", "depense", "document", "document", "espace", "espace", "idee", "jour", "jour", "ligne", "ligne", "moment", "operation", "operation", "page", "page", "prelevement", "prelevement", "relever", "relever", "service", "service", "trouver", "trouver", "virement"]}, "R": 10, "lambda.step": 0.01, "plot.opts": {"xlab": "PC1", "ylab": "PC2"}, "topic.order": [1, 2]};

app.layout = html.Div([
    pyldavis_dash.pyLDAvis(id='1', data=data),
])

if __name__ == '__main__':
    app.run_server(debug=True)
