using System.IO;
using System.Threading.Tasks;
using CatalogoAPI.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Extensions.Http;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Logging;
using Newtonsoft.Json;

namespace CatalogoAPI.Functions
{
    public static class SalvarRegistroFunction
    {
        [FunctionName("SalvarRegistro")]
        public static async Task<IActionResult> Run(
            [HttpTrigger(AuthorizationLevel.Function, "post", Route = null)] HttpRequest req,
            [CosmosDB(
                databaseName: "CatalogosDB",
                containerName: "Catalogos",
                Connection = "CosmosDBConnection")] IAsyncCollector<CatalogoItem> documentos,
            ILogger log)
        {
            string requestBody = await new StreamReader(req.Body).ReadToEndAsync();
            var data = JsonConvert.DeserializeObject<CatalogoItem>(requestBody);

            await documentos.AddAsync(data);

            return new OkObjectResult("Registro salvo com sucesso.");
        }
    }
}
