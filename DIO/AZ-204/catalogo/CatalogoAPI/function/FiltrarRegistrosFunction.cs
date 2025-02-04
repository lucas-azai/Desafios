using System.Collections.Generic;
using CatalogoAPI.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Extensions.Http;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Logging;

namespace CatalogoAPI.Functions
{
    public static class FiltrarRegistrosFunction
    {
        [FunctionName("FiltrarRegistros")]
        public static IActionResult Run(
            [HttpTrigger(AuthorizationLevel.Function, "get", Route = "catalogos/{genero}")] HttpRequest req,
            [CosmosDB(
                databaseName: "CatalogosDB",
                containerName: "Catalogos",
                SqlQuery = "SELECT * FROM c WHERE c.Genero = {genero}",
                Connection = "CosmosDBConnection")] IEnumerable<CatalogoItem> resultados,
            ILogger log)
        {
            return new OkObjectResult(resultados);
        }
    }
}
