using System.Collections.Generic;
using CatalogoAPI.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Extensions.Http;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Logging;

namespace CatalogoAPI.Functions
{
    public static class ListarRegistrosFunction
    {
        [FunctionName("ListarRegistros")]
        public static IActionResult Run(
            [HttpTrigger(AuthorizationLevel.Function, "get", Route = "catalogos")] HttpRequest req,
            [CosmosDB(
                databaseName: "CatalogosDB",
                containerName: "Catalogos",
                SqlQuery = "SELECT * FROM c",
                Connection = "CosmosDBConnection")] IEnumerable<CatalogoItem> documentos,
            ILogger log)
        {
            return new OkObjectResult(documentos);
        }
    }
}
