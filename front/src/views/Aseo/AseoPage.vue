<template>

    <div class="botonesIzquierda">
        <button class="generalBotonIz" id="azulOscuro">Ducharse</button><br><br>
        <button class="generalBotonIz" id="morado">Cepillarse los dientes</button><br><br>
        <button class="generalBotonIz" id="verde">Vestirse</button><br><br>

    </div>
    
</template>

ddd
<style scoped>

    *  {
        background-color: white;
        width: 100%;
        height: 77vh;
    }

    .generalBotonIz {
        Width: 9rem;
        Height: 1.9rem; 
        border-radius: 10px; 
        border-style: none;
        margin:30px 70px;

    }

    .generalBotonDe {
        Width: 9rem;
        Height: 1.9rem; 
        border-radius: 10px; 
        border-style: none;
        display: flex;
        justify-content: center;

    }


    .botonesIzquierda{
        display: flex;
        justify-content: flex-start;
    }


    #azulOscuro{
        background-color: #5266CE

    }

    #morado{
        background-color: #CE52C2;
    }

    #verde{
        background-color: #73CE52;
    }

    #azulClaro{
        background-color: #7EBFD3;

    }


</style>