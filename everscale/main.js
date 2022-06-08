const { TonClient } = require("@eversdk/core");
const {libNode} = require("@eversdk/lib-node");
const PythonShell = require('python-shell').PythonShell;


TonClient.useBinaryLibrary(libNode);

const client = new TonClient({
    network: { 
        endpoints: ['https://eri01.main.everos.dev/']
    } 
});

async function get_coffe_machine_transactions() {
    return await client.net.query({
        query: `{
            blockchain{
            account(address:"0:34f36279f650b703e306e6f5bb200d4f47e7852f34da01667c08e8769e601801"){
            transactions{
                edges{
                node{
                    id
                    hash
                    in_msg
                    out_msgs
                    balance_delta(format:DEC)
                    total_fees(format:DEC)
                }
                }
                pageInfo{
                endCursor
                hasNextPage
                }
            }
            }
            }
        }`,
    });
}

(async () => {

    txs = await get_coffe_machine_transactions();
    txs_count = txs.result.data.blockchain.account.transactions.edges.length;
    console.log(`Transactions count: ${txs_count}`);
    // console.log(txs.result.data.blockchain.account.transactions.edges[txs_count - 1]);
    // console.log(txs.result.data.blockchain.account.transactions.edges[txs_count - 1].node)
    while (true) {
        try {
            txs = await get_coffe_machine_transactions();
            txs = txs.result.data.blockchain.account.transactions.edges;
            if (txs.length > txs_count) {
                console.log('Transaction catched!');
                tx = txs[txs_count - 1].node;
                if (tx.total_fees + tx.balance_delta >= 0.5 * Math.pow(10, 9)) {
                    PythonShell.run('make_coffe.py', null, function (err) {
                        if (err) throw err;
                        console.log('finished');
                    });
                }
                txs_count = txs.length;
            }
        }
        catch {
            console.log('Somethong goes wrong!')
        }
    }
})();