import os

def generateRepository():
  listEntities = ["ConnectionLog", "Equipment", "Hof", "Item", "ItemFamily", "Lot", "Material", "Of", "Order", "Process", "ServiceEntity", "Setting", "Standard", "Step", "Supply", "User", "Zone"]

  for(entity) in listEntities:
    suffix = "Repository"
    extension = ".java"
    nameFile = entity + suffix + extension
    file = open(nameFile, "w")
    file.write("package com.d4care.dome.repositories;")
    file.write("\n")
    file.write("\n")
    file.write("import com.d4care.dome.entities." + entity + ";")
    file.write("\n")
    file.write("import org.springframework.data.jpa.repository.JpaRepository;")
    file.write("\n")
    file.write("import org.springframework.stereotype.Repository;")
    file.write("\n")
    file.write("\n")
    file.write("@Repository")
    file.write("\n")
    file.write("public interface " + entity + suffix + " extends JpaRepository<" + entity + ",Long> {")
    file.write("\n")
    file.write("\n")
    file.write("  // Todo")
    file.write("\n")
    file.write("\n")
    file.write("}")
    file.write("\n")


def generateServices():
  listEntities = ["ConnectionLog", "Equipment", "Hof", "Item", "ItemFamily", "Lot", "Material", "Of", "Order", "Process", "ServiceEntity", "Setting", "Standard", "Step", "Supply", "User", "Zone"]

  for(entity) in listEntities:
    suffix = "Service"
    extension = ".java"
    nameFile = entity + suffix + extension
    file = open(nameFile, "w")
    file.write("package com.d4care.dome.services;")
    file.write("\n")
    file.write("\n")
    file.write("import com.d4care.dome.entities." + entity + ";")
    file.write("\n")
    file.write("\n")
    file.write("import org.springframework.web.server.ResponseStatusException;")
    file.write("\n")
    file.write("\n")
    file.write("import java.util.List;")
    file.write("\n")
    file.write("\n")
    file.write("public interface " + entity + "Service {")
    file.write("\n")
    file.write("\n")
    file.write("    // Todo")
    file.write("\n")
    file.write("\n")
    file.write("\n")
    file.write("}")
    file.write("\n")


def generateServicesImpl():
  listEntities = ["ConnectionLog", "Equipment", "Hof", "Item", "ItemFamily", "Lot", "Material", "Of", "Order", "Process", "ServiceEntity", "Setting", "Standard", "Step", "Supply", "User", "Zone"]

  for(entity) in listEntities:
    suffix = "ServiceImpl"
    extension = ".java"
    nameFile = entity + suffix + extension
    file = open(nameFile, "w")
    file.write("package com.d4care.dome.services;")
    file.write("\n")
    file.write("\n")
    file.write("import com.d4care.dome.dto." + entity + "Dto;")
    file.write("\n")
    file.write("import com.d4care.dome.entities." + entity + ";")
    file.write("\n")
    file.write("import com.d4care.dome.repositories." + entity + "Repository;")
    file.write("\n")
    file.write("import org.springframework.stereotype.Service;")
    file.write("\n")
    file.write("\n")
    file.write("import static com.d4care.dome.utils.Constantes.ErrorMessage.*;")
    file.write("\n")
    file.write("\n")
    file.write("@Service")
    file.write("\n")
    file.write("public class " + entity + "ServiceImpl implements " + entity + "Service {")
    file.write("\n")
    file.write("\n")
    file.write("    @Autowired")
    file.write("\n")
    file.write("    private " + entity + "Repository " + entity + "Repository;")
    file.write("\n")
    file.write("\n")
    file.write("    // Todo")
    file.write("\n")
    file.write("\n")
    file.write("}")
    file.write("\n")



def generateControllers():
  listEntities = ["ConnectionLog", "Equipment", "Hof", "Item", "ItemFamily", "Lot", "Material", "Of", "Order", "Process","Product", "Service", "Setting", "Standard", "Step", "Supply", "User", "Zone"]

  for(entity) in listEntities:
    suffix = "Controller"
    extension = ".java"
    nameFile = entity + suffix + extension
    file = open(nameFile, "w")
    file.write("package com.d4care.dome.controllers;")
    file.write("\n")
    file.write("\n")
    file.write("import org.springframework.web.bind.annotation.RequestMapping;")
    file.write("\n")
    file.write("import org.springframework.web.bind.annotation.RestController;")
    file.write("\n")
    file.write("\n")
    file.write("@RestController")
    file.write("\n")
    file.write('@RequestMapping("/' + entity + 's")')
    file.write("\n")
    file.write("public class " + entity + "Controller {")
    file.write("\n")
    file.write("\n")
    file.write("  // Todo")
    file.write("\n")
    file.write("\n")
    file.write("}")
    file.write("\n")


def generateFunctionModelMapper():
  listEntities = ["ConnectionLog", "Equipment", "Hof", "Item", "ItemFamily", "Lot", "Material", "Of", "Order", "Process","Product", "Service", "Setting", "Standard", "Step", "Supply", "User", "Zone"]
  file = open("ModelMapperFuction.java", "w")

  for(entity) in listEntities:
    file.write(entity + "Dto convertToDto(" + entity + " " + entity.lower() + ");")
    file.write("\n")
    file.write(entity + " convertToDao(" + entity + "Dto " + entity.lower() + "Dto);")
    file.write("\n")
    file.write("\n")


def generateFunctionModelMapperImpl():
  listEntities = ["ConnectionLog", "Equipment", "Hof", "Item", "ItemFamily", "Lot", "Material", "Of", "Order", "Process","Product", "Service", "Setting", "Standard", "Step", "Supply", "User", "Zone"]
  file = open("ModelMapperFuctionImpl.java", "w")

  for(entity) in listEntities:
    file.write("@Override")
    file.write("\n")
    file.write("public " + entity + "Dto convertToDto(" + entity + " " + entity.lower() + ") {")
    file.write("\n")
    file.write("    return modelMapper.map(" + entity.lower() + ", " + entity + "Dto.class);")
    file.write("\n")
    file.write("}")
    file.write("\n")
    file.write("\n")
    file.write("@Override")
    file.write("\n")
    file.write("public " + entity + " convertToDao(" + entity + "Dto " + entity.lower() + "Dto) {")
    file.write("\n")
    file.write("    return modelMapper.map(" + entity.lower() + "Dto, " + entity + ".class);")
    file.write("\n")
    file.write("}")
    file.write("\n")
    file.write("\n")
