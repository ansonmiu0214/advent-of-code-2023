// project
#include <aoclib_solutionsrunner.h>

// stdlib
#include <cassert>
#include <climits>
#include <format>
#include <functional>
#include <numeric>
#include <iostream>
#include <string>
#include <vector>

namespace {

std::vector<int> groupCaloriesByElf(const std::vector<std::string> &lines)
{
    std::vector<int> caloriesByElf;

    int caloriesForCurrentElf = 0;
    for (const auto &line : lines) {
        if (line.empty()) {
            caloriesByElf.push_back(caloriesForCurrentElf);
            caloriesForCurrentElf = 0;
        }
        else {
            caloriesForCurrentElf += std::stoi(line);
        }
    }

    // Don't forget the last elf(!)

    if (caloriesForCurrentElf > 0) {
        caloriesByElf.push_back(caloriesForCurrentElf);
    }

    return caloriesByElf;
}

int findElfWithMostCalories(const std::vector<int>& caloriesByElf)
{
    return std::accumulate(caloriesByElf.cbegin(),
                           caloriesByElf.cend(),
                           INT_MIN,
                           std::ranges::max);
}

int part1(const std::vector<std::string> &lines)
{
    const auto &caloriesByElf = groupCaloriesByElf(lines);
    assert(!caloriesByElf.empty());

    return findElfWithMostCalories(caloriesByElf);
}

template <unsigned int N>
int totalCaloriesAmongElvesWithMostCalories(std::vector<int> caloriesByElf)
{
    std::partial_sort(caloriesByElf.begin(),
                      caloriesByElf.begin() + N,
                      caloriesByElf.end(),
                      std::greater{});

    return std::accumulate(caloriesByElf.cbegin(),
                           caloriesByElf.cbegin() + N,
                           0);   
}

int part2(const std::vector<std::string> &lines)
{
    auto caloriesByElf = groupCaloriesByElf(lines);
    assert(!caloriesByElf.empty());

    return totalCaloriesAmongElvesWithMostCalories<3>(caloriesByElf);
}

std::string formatAnswer(int calories)
{
    return std::format("{:L} calories", calories);
}

}   // closing unnamed namespace

int main(int argc, char const *argv[])
{
    return aoclib::SolutionsRunner{part1, part2, formatAnswer}.main(argc, argv);
}